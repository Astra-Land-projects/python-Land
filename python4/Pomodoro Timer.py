import 'dart:async';
import 'package:flutter/material.dart';

void main() => runApp(const PomodoroApp());

class PomodoroApp extends StatelessWidget {
  const PomodoroApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const PomodoroPage(),
    );
  }
}

class PomodoroPage extends StatefulWidget {
  const PomodoroPage({super.key});

  @override
  State<PomodoroPage> createState() =>
      _PomodoroPageState();
}

class _PomodoroPageState
    extends State<PomodoroPage> {

  int seconds = 25 * 60;
  Timer? timer;

  void start() {
    timer?.cancel();

    timer = Timer.periodic(
      const Duration(seconds: 1),
      (_) {
        if (seconds <= 0) {
          timer?.cancel();
          return;
        }

        setState(() {
          seconds--;
        });
      },
    );
  }

  void reset() {
    timer?.cancel();

    setState(() {
      seconds = 25 * 60;
    });
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final minutes =
        (seconds ~/ 60).toString().padLeft(2, "0");

    final secs =
        (seconds % 60).toString().padLeft(2, "0");

    return Scaffold(
      appBar: AppBar(
        title: const Text("Pomodoro"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment:
              MainAxisAlignment.center,
          children: [
            Text(
              "$minutes:$secs",
              style: const TextStyle(
                fontSize: 60,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            Wrap(
              spacing: 10,
              children: [
                ElevatedButton(
                  onPressed: start,
                  child: const Text("Start"),
                ),
                ElevatedButton(
                  onPressed: reset,
                  child: const Text("Reset"),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}