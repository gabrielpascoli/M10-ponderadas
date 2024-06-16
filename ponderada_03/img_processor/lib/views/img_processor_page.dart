import 'dart:io';
import 'package:flutter/material.dart';
import 'package:img_processor/controllers/img_processor_controller.dart';

class ImgProcessorPage extends StatefulWidget {
  final String? username;
  final String? email;

  ImgProcessorPage({this.username, this.email});

  @override
  _ImgProcessorPageState createState() => _ImgProcessorPageState(username, email);
}

class _ImgProcessorPageState extends State<ImgProcessorPage> {
  final String? username;
  final String? email;
  final ImgProcessorController _imgProcessorController = ImgProcessorController();
  File? _image;
  File? _filteredImage;
  bool _isLoading = false;

  _ImgProcessorPageState(this.username, this.email);

  void _setImage(File? image) {
    setState(() {
      _image = image;
    });
  }

  void _setFilteredImage(File? filteredImage) {
    setState(() {
      _filteredImage = filteredImage;
    });
  }

  void _setLoading(bool isLoading) {
    setState(() {
      _isLoading = isLoading;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Processador de Imagens'),
        flexibleSpace: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [Colors.blue, Colors.green],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              if (_image != null)
                Card(
                  elevation: 5,
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Image.file(_image!),
                  ),
                ),
              if (_filteredImage != null)
                Card(
                  elevation: 5,
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Image.file(_filteredImage!),
                  ),
                ),
              SizedBox(height: 20),
              ElevatedButton.icon(
                onPressed: () {
                  _imgProcessorController.pickImage(
                    username,
                    email,
                    _setImage,
                    _setFilteredImage,
                  );
                },
                icon: Icon(Icons.image),
                label: Text('Selecionar Imagem'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blue,
                  padding: EdgeInsets.symmetric(vertical: 16.0),
                  textStyle: TextStyle(fontSize: 16),
                ),
              ),
              SizedBox(height: 10),
              ElevatedButton.icon(
                onPressed: () {
                  _imgProcessorController.uploadImage(
                    username,
                    email,
                    _image,
                    _setLoading,
                    _setFilteredImage,
                  );
                },
                icon: Icon(Icons.upload),
                label: _isLoading ? CircularProgressIndicator(color: Colors.white) : Text('Aplicar Filtro'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.green,
                  padding: EdgeInsets.symmetric(vertical: 16.0),
                  textStyle: TextStyle(fontSize: 16),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}