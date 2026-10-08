import 'package:flutter/material.dart';

void main() => runApp(const MemoryApp());

class MemoryApp extends StatelessWidget {
  const MemoryApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const MemoryPage(),
    );
  }
}

class MemoryPage extends StatefulWidget {
  const MemoryPage({super.key});

  @override
  State<MemoryPage> createState() =>
      _MemoryPageState();
}

class _MemoryPageState
    extends State<MemoryPage> {

  final cards = [
    "🐶",
    "🐱",
    "🐭",
    "🐹",
    "🐰",
    "🦊",
  ];

  final opened = <int>{};

  void openCard(int index) {
    setState(() {
      if (opened.contains(index)) {
        opened.remove(index);
      } else {
        opened.add(index);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Memory Game"),
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(16),
        gridDelegate:
            const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
        ),
        itemCount: cards.length,
        itemBuilder: (_, index) {
          final visible =
              opened.contains(index);

          return GestureDetector(
            onTap: () => openCard(index),
            child: Card(
              child: Center(
                child: Text(
                  visible ? cards[index] : "❓",
                  style: const TextStyle(
                    fontSize: 40,
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}