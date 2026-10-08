import 'package:flutter/material.dart';

void main() => runApp(const BubbleApp());

class BubbleApp extends StatelessWidget {
  const BubbleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text("Chat UI")),
        body: ListView(
          padding: const EdgeInsets.all(16),
          children: const [
            Align(
              alignment: Alignment.centerLeft,
              child: Chip(label: Text("Hello!")),
            ),
            Align(
              alignment: Alignment.centerRight,
              child: Chip(label: Text("Hi there!")),
            ),
          ],
        ),
      ),
    );
  }
}