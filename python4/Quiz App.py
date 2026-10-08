import 'package:flutter/material.dart';

void main() => runApp(const QuizApp());

class QuizApp extends StatelessWidget {
  const QuizApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const QuizPage(),
    );
  }
}

class QuizPage extends StatefulWidget {
  const QuizPage({super.key});

  @override
  State<QuizPage> createState() => _QuizPageState();
}

class _QuizPageState extends State<QuizPage> {
  int score = 0;

  final question =
      "Which language is used by Flutter?";

  final answers = [
    "Python",
    "Dart",
    "Java",
    "C++",
  ];

  void answer(String value) {
    setState(() {
      if (value == "Dart") {
        score++;
      }
    });

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          value == "Dart"
              ? "Correct!"
              : "Wrong!",
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Quiz — Score: $score"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            Text(
              question,
              style: const TextStyle(
                fontSize: 24,
              ),
            ),
            const SizedBox(height: 30),
            ...answers.map(
              (answer) => Padding(
                padding:
                    const EdgeInsets.all(5),
                child: SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () =>
                        answer == "Dart"
                            ? answer
                            : answer,
                    child: Text(answer),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}