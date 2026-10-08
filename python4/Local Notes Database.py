import 'package:flutter/material.dart';

void main() => runApp(const DatabaseNotesApp());

class DatabaseNotesApp extends StatelessWidget {
  const DatabaseNotesApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const NotesDatabasePage(),
    );
  }
}

class NotesDatabasePage extends StatefulWidget {
  const NotesDatabasePage({super.key});

  @override
  State<NotesDatabasePage> createState() =>
      _NotesDatabasePageState();
}

class _NotesDatabasePageState
    extends State<NotesDatabasePage> {

  final controller = TextEditingController();

  final notes = <String>[];

  void addNote() {
    if (controller.text.trim().isEmpty) return;

    setState(() {
      notes.add(controller.text.trim());
      controller.clear();
    });
  }

  void deleteNote(int index) {
    setState(() {
      notes.removeAt(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Notes Database"),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: controller,
                  ),
                ),
                IconButton(
                  onPressed: addNote,
                  icon: const Icon(Icons.add),
                ),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: notes.length,
              itemBuilder: (_, index) {
                return ListTile(
                  title: Text(notes[index]),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    onPressed: () =>
                        deleteNote(index),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}