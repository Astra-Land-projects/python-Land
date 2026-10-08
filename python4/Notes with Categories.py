import 'package:flutter/material.dart';

void main() => runApp(const CatNotesApp());

class CatNotesApp extends StatelessWidget {
  const CatNotesApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const CatNotesPage(),
    );
  }
}

class CatNotesPage extends StatefulWidget {
  const CatNotesPage({super.key});

  @override
  State<CatNotesPage> createState() => _CatNotesPageState();
}

class _CatNotesPageState extends State<CatNotesPage> {
  final notes = <Map<String, String>>[
    {"title": "Study Python", "cat": "Learning"},
    {"title": "Build Telegram bot", "cat": "Project"},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Categorized Notes")),
      body: ListView.builder(
        itemCount: notes.length,
        itemBuilder: (_, i) => Card(
          child: ListTile(
            title: Text(notes[i]["title"]!),
            subtitle: Text(notes[i]["cat"]!),
          ),
        ),
      ),
    );
  }
}