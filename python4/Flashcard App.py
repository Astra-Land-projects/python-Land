import 'package:flutter/material.dart';

void main() => runApp(const FlashcardApp());

class FlashcardApp extends StatelessWidget {
  const FlashcardApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const FlashcardPage(),
    );
  }
}

class FlashcardPage extends StatefulWidget {
  const FlashcardPage({super.key});

  @override
  State<FlashcardPage> createState() =>
      _FlashcardPageState();
}

class _FlashcardPageState
    extends State<FlashcardPage> {

  bool showAnswer = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Flashcards"),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () {
            setState(() {
              showAnswer = !showAnswer;
            });
          },
          child: Card(
            child: SizedBox(
              width: 300,
              height: 200,
              child: Center(
                child: Text(
                  showAnswer
                      ? "Dart"
                      : "What language does Flutter use?",
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                    fontSize: 22,
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}