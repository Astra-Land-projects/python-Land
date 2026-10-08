import 'package:flutter/material.dart';

void main() => runApp(const ProfileApp());

class ProfileApp extends StatelessWidget {
  const ProfileApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text("Profile")),
        body: const Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              CircleAvatar(radius: 50, child: Icon(Icons.person, size: 50)),
              SizedBox(height: 16),
              Text("Arya Gh", style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
              Text("Python • AI • Flutter"),
            ],
          ),
        ),
      ),
    );
  }
}