import 'package:flutter/material.dart';

void main() => runApp(const AssistantApp());

class AssistantApp extends StatelessWidget {
  const AssistantApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const AssistantPage(),
    );
  }
}

class AssistantPage extends StatefulWidget {
  const AssistantPage({super.key});

  @override
  State<AssistantPage> createState() => _AssistantPageState();
}

class _AssistantPageState extends State<AssistantPage> {
  final controller = TextEditingController();
  String answer = "Ask me something.";

  void ask() {
    final q = controller.text.toLowerCase().trim();
    if (q.isEmpty) return;

    setState(() {
      if (q.contains("time")) {
        answer = "I can show time later when connected to an AI/API.";
      } else if (q.contains("hello")) {
        answer = "Hello! I'm your mobile assistant.";
      } else {
        answer = "This is a placeholder AI assistant UI.";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("AI Assistant")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: controller,
              decoration: const InputDecoration(
                hintText: "Ask anything",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 12),
            ElevatedButton(onPressed: ask, child: const Text("Ask")),
            const SizedBox(height: 20),
            Text(answer, style: const TextStyle(fontSize: 18)),
          ],
        ),
      ),
    );
  }
}