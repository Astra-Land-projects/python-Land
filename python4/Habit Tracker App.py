import 'package:flutter/material.dart';

void main() => runApp(const HabitApp());

class HabitApp extends StatelessWidget {
  const HabitApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const HabitPage(),
    );
  }
}

class HabitPage extends StatefulWidget {
  const HabitPage({super.key});

  @override
  State<HabitPage> createState() => _HabitPageState();
}

class _HabitPageState extends State<HabitPage> {
  final controller = TextEditingController();
  final List<Map<String, dynamic>> habits = [];

  void addHabit() {
    final text = controller.text.trim();
    if (text.isEmpty) return;
    setState(() {
      habits.add({"title": text, "done": false});
      controller.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Habit Tracker")),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: controller,
                    decoration: const InputDecoration(
                      hintText: "New habit",
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                ElevatedButton(onPressed: addHabit, child: const Text("Add")),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: habits.length,
              itemBuilder: (context, index) {
                final habit = habits[index];
                return CheckboxListTile(
                  title: Text(habit["title"]),
                  value: habit["done"],
                  onChanged: (value) {
                    setState(() => habit["done"] = value ?? false);
                  },
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}