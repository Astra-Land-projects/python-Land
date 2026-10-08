import 'dart:math';
import 'package:flutter/material.dart';

void main() => runApp(const RpsApp());

class RpsApp extends StatefulWidget {
  const RpsApp({super.key});

  @override
  State<RpsApp> createState() => _RpsAppState();
}

class _RpsAppState extends State<RpsApp> {
  final choices = ["Rock", "Paper", "Scissors"];

  String result = "Choose one";

  void play(String player) {
    final computer =
        choices[Random().nextInt(3)];

    String message;

    if (player == computer) {
      message = "Draw! Computer: $computer";
    } else if (
        (player == "Rock" && computer == "Scissors") ||
        (player == "Paper" && computer == "Rock") ||
        (player == "Scissors" && computer == "Paper")) {
      message = "You win! Computer: $computer";
    } else {
      message = "Computer wins! Computer: $computer";
    }

    setState(() {
      result = message;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text("Rock Paper Scissors"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment:
                MainAxisAlignment.center,
            children: [
              Text(
                result,
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 20),
              ...choices.map(
                (choice) => ElevatedButton(
                  onPressed: () => play(choice),
                  child: Text(choice),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}