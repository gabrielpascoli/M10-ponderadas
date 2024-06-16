import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:img_processor/services/notifi.dart';
import 'package:img_processor/views/img_processor_page.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class LoginController {
  Future<void> login(
    BuildContext context, 
    TextEditingController usernameController, 
    TextEditingController passwordController, 
    Function setState, 
    Function setLoading, 
    Function setErrorMessage
  ) async {
    setLoading(true);
    setErrorMessage('');

    try {
      final String? url = dotenv.env['URL'];
      final String? userMgmt = dotenv.env['USER_MGMT'];

      final response = await http.post(
        Uri.parse('$url/$userMgmt/login'),
        body: jsonEncode({
          'username': usernameController.text,
          'password': passwordController.text,
        }),
        headers: {'Content-Type': 'application/json'},
      );

      setLoading(false);

      if (response.statusCode >= 200 && response.statusCode < 300) {
        final data = jsonDecode(response.body);
        final String? username = data['username'];
        final String? email = data['email'];

        NotificationService.showNotification('Login Successful', 'Welcome back, $username!');

        final String? logger = dotenv.env['LOGGER'];
        await http.post(
          Uri.parse('$url/$logger/log'),
          body: jsonEncode({
            'username': username,
            'email': email,
            'action': 'login',
            'datetime': DateTime.now().toIso8601String(),
          }),
          headers: {'Content-Type': 'application/json'},
        );

        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ImgProcessorPage(username: username, email: email),
          ),
        );
      } else {
        setErrorMessage('Invalid username or password');
      }
    } catch (e) {
      setLoading(false);
      setErrorMessage('Failed to login');
    }
  }
}
