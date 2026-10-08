import 'dart:math';
import 'package:flutter/material.dart';

void main() => runApp(const DiceApp());

class DiceApp extends StatefulWidget {
  const DiceApp({super.key});

  @override
  State<DiceApp> createState() => _DiceAppState();
}

class _DiceAppState extends State<DiceApp> {
  int dice = 1;

  void roll() {
    setState(() {
      dice = Random().nextInt(6) + 1;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text("Dice Game"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment:
                MainAxisAlignment.center,
            children: [
              Text(
                "🎲 $dice",
                style: const TextStyle(
                  fontSize: 70,
                ),
              ),
              ElevatedButton(
                onPressed: roll,
                child: const Text("Roll"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}