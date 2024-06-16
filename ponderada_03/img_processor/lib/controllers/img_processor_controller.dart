import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';
import 'package:img_processor/services/notifi.dart';
import 'package:path/path.dart' as path;
import 'package:flutter_dotenv/flutter_dotenv.dart';

class ImgProcessorController {
  final ImagePicker _picker = ImagePicker();

  Future<void> pickImage(
    String? username, 
    String? email, 
    Function setImage, 
    Function setFilteredImage
  ) async {
    final pickedFile = await _picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      setImage(File(pickedFile.path));
      setFilteredImage(null);

      final String? url = dotenv.env['URL'];
      final String? logger = dotenv.env['LOGGER'];
      await http.post(
        Uri.parse('$url/$logger/log'),
        body: jsonEncode({
          'username': username,
          'email': email,
          'action': 'image_picked',
          'datetime': DateTime.now().toIso8601String(),
        }),
        headers: {'Content-Type': 'application/json'},
      );

      NotificationService.showNotification('Image Picked', 'Image has been picked');
    }
  }

  Future<void> uploadImage(
    String? username, 
    String? email, 
    File? image, 
    Function setLoading, 
    Function setFilteredImage
  ) async {
    if (image == null) return;

    setLoading(true);

    final String? url = dotenv.env['URL'];
    final String? imgFilter = dotenv.env['IMG_FILTER'];

    var request = http.MultipartRequest('POST', Uri.parse('$url/$imgFilter/upload'));
    request.files.add(await http.MultipartFile.fromPath('file', image.path));

    var response = await request.send();
    if (response.statusCode == 200) {
      var responseData = await response.stream.toBytes();
      var tempDir = await getTemporaryDirectory();
      var filePath = path.join(tempDir.path, 'filtered_image.jpg');
      File file = File(filePath);
      await file.writeAsBytes(responseData);
      setFilteredImage(file);
      setLoading(false);

      final String? logger = dotenv.env['LOGGER'];
      await http.post(
        Uri.parse('$url/$logger/log'),
        body: jsonEncode({
          'username': username,
          'email': email,
          'action': 'image_filtered',
          'datetime': DateTime.now().toIso8601String(),
        }),
        headers: {'Content-Type': 'application/json'},
      );

      NotificationService.showNotification('Image Filtered', 'Image has been filtered');
    } else {
      setLoading(false);
    }
  }
}
