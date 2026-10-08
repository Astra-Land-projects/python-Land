import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() => runApp(const StorageApp());

class StorageApp extends StatelessWidget {
  const StorageApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const StoragePage(),
    );
  }
}

class StoragePage extends StatefulWidget {
  const StoragePage({super.key});

  @override
  State<StoragePage> createState() => _StoragePageState();
}

class _StoragePageState extends State<StoragePage> {
  final controller = TextEditingController();

  String saved = "";

  Future<void> save() async {
    final prefs = await SharedPreferences.getInstance();

    await prefs.setString(
      "message",
      controller.text,
    );

    load();
  }

  Future<void> load() async {
    final prefs = await SharedPreferences.getInstance();

    setState(() {
      saved = prefs.getString("message") ?? "";
    });
  }

  @override
  void initState() {
    super.initState();
    load();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Local Storage")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(controller: controller),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: save,
              child: const Text("Save"),
            ),
            const SizedBox(height: 20),
            Text("Saved: $saved"),
          ],
        ),
      ),
    );
  }
}