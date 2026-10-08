import 'package:flutter/material.dart';

void main() => runApp(const SearchApp());

class SearchApp extends StatelessWidget {
  const SearchApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const SearchPage(),
    );
  }
}

class SearchPage extends StatefulWidget {
  const SearchPage({super.key});

  @override
  State<SearchPage> createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  final controller = TextEditingController();
  final items = ["Python", "Flutter", "FastAPI", "TensorFlow", "Git"];
  List<String> filtered = [];

  @override
  void initState() {
    super.initState();
    filtered = items;
  }

  void search(String q) {
    setState(() {
      filtered = items.where((e) => e.toLowerCase().contains(q.toLowerCase())).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Search")),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(
              controller: controller,
              onChanged: search,
              decoration: const InputDecoration(border: OutlineInputBorder(), hintText: "Search..."),
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: filtered.length,
              itemBuilder: (_, i) => ListTile(title: Text(filtered[i])),
            ),
          ),
        ],
      ),
    );
  }
}