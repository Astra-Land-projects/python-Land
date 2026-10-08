import 'package:flutter/material.dart';

void main() => runApp(const ProgressApp());

class ProgressApp extends StatelessWidget {
  const ProgressApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const ProgressPage(),
    );
  }
}

class ProgressPage extends StatelessWidget {
  const ProgressPage({super.key});

  @override
  Widget build(BuildContext context) {
    const progress = 0.72;

    return Scaffold(
      appBar: AppBar(
        title: const Text("Progress"),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(30),
          child: Column(
            mainAxisAlignment:
                MainAxisAlignment.center,
            children: [
              const Text(
                "Project Progress",
                style: TextStyle(fontSize: 24),
              ),
              const SizedBox(height: 20),
              LinearProgressIndicator(
                value: progress,
                minHeight: 15,
              ),
              const SizedBox(height: 15),
              Text("${(progress * 100).round()}%"),
            ],
          ),
        ),
      ),
    );
  }
}