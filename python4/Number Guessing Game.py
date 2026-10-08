import 'dart:math';
import 'package:flutter/material.dart';

void main() => runApp(const GuessApp());

class GuessApp extends StatelessWidget {
  const GuessApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const GuessPage(),
    );
  }
}

class GuessPage extends StatefulWidget {
  const GuessPage({super.key});

  @override
  State<GuessPage> createState() =>
      _GuessPageState();
}

class _GuessPageState
    extends State<GuessPage> {

  final controller = TextEditingController();

  int target =
      Random().nextInt(100) + 1;

  String message =
      "Guess a number between 1 and 100.";

  void guess() {
    final value =
        int.tryParse(controller.text);

    if (value == null) return;

    setState(() {
      if (value == target) {
        message = "🎉 Correct!";
      } else if (value < target) {
        message = "Too low!";
      } else {
        message = "Too high!";
      }
    });
  }

  void restart() {
    setState(() {
      target =
          Random().nextInt(100) + 1;
      message =
          "Guess a number between 1 and 100.";
      controller.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Guessing Game"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment:
              MainAxisAlignment.center,
          children: [
            Text(
              message,
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 22,
              ),
            ),
            TextField(
              controller: controller,
              keyboardType:
                  TextInputType.number,
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: guess,
              child: const Text("Guess"),
            ),
            TextButton(
              onPressed: restart,
              child: const Text("Restart"),
            ),
          ],
        ),
      ),
    );
  }
}
