import 'dart:math';
import 'package:flutter/material.dart';

void main() => runApp(const ReactionApp());

class ReactionApp extends StatelessWidget {
  const ReactionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const ReactionPage(),
    );
  }
}

class ReactionPage extends StatefulWidget {
  const ReactionPage({super.key});

  @override
  State<ReactionPage> createState() =>
      _ReactionPageState();
}

class _ReactionPageState
    extends State<ReactionPage> {

  bool active = false;
  String result = "Press Start";

  void start() {
    Future.delayed(
      Duration(
        milliseconds:
            Random().nextInt(3000) + 1000,
      ),
      () {
        if (!mounted) return;

        setState(() {
          active = true;
          result = "TAP!";
        });
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: GestureDetector(
        onTap: active
            ? () {
                setState(() {
                  active = false;
                  result = "Good reaction!";
                });
              }
            : null,
        child: Center(
          child: Column(
            mainAxisAlignment:
                MainAxisAlignment.center,
            children: [
              Text(
                result,
                style: const TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: start,
                child: const Text("Start"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}