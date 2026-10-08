import 'package:flutter/material.dart';

void main() {
  runApp(const ChatApp());
}

class ChatApp extends StatelessWidget {
  const ChatApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Chat',
      theme: ThemeData(
        useMaterial3: true,
      ),
      home: const ChatPage(),
    );
  }
}

class ChatPage extends StatefulWidget {
  const ChatPage({super.key});

  @override
  State<ChatPage> createState() =>
      _ChatPageState();
}

class _ChatPageState
    extends State<ChatPage> {

  final controller =
      TextEditingController();

  final List<String> messages = [];

  void send() {
    final text =
        controller.text.trim();

    if (text.isEmpty) {
      return;
    }

    setState(() {
      messages.add(text);
      controller.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Chat'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (
                context,
                index,
              ) {
                return ListTile(
                  leading:
                      const CircleAvatar(
                    child: Icon(Icons.person),
                  ),
                  title:
                      Text(messages[index]),
                );
              },
            ),
          ),
          Padding(
            padding:
                const EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: controller,
                    decoration:
                        const InputDecoration(
                      hintText: 'Message',
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