import 'package:flutter/material.dart';

void main() => runApp(const SimpleAiApp());

class SimpleAiApp extends StatelessWidget {
  const SimpleAiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const AiChatPage(),
    );
  }
}

class AiChatPage extends StatefulWidget {
  const AiChatPage({super.key});

  @override
  State<AiChatPage> createState() =>
      _AiChatPageState();
}

class _AiChatPageState
    extends State<AiChatPage> {

  final controller = TextEditingController();

  final messages = <Map<String, String>>[];

  void send() {
    final text =
        controller.text.trim();

    if (text.isEmpty) return;

    setState(() {
      messages.add({
        "role": "user",
        "text": text,
      });

      messages.add({
        "role": "ai",
        "text": generateReply(text),
      });

      controller.clear();
    });
  }

  String generateReply(String text) {
    final q = text.toLowerCase();

    if (q.contains("hello")) {
      return "Hello! 👋";
    }

    if (q.contains("python")) {
      return "Python is a powerful programming language.";
    }

    if (q.contains("flutter")) {
      return "Flutter is used to build cross-platform apps.";
    }

    return "I don't know that yet.";
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("AI Chat"),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (_, index) {
                final message =
                    messages[index];

                return ListTile(
                  title: Text(
                    message["role"] == "ai"
                        ? "AI"
                        : "You",
                  ),
                  subtitle:
                      Text(message["text"]!),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: controller,
                    decoration:
                        const InputDecoration(
                      hintText: "Ask AI...",
                      border:
                          OutlineInputBorder(),
                    ),
                  ),
                ),
                IconButton(
                  onPressed: send,
                  icon:
                      const Icon(Icons.send),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}