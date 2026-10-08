import 'package:flutter/material.dart';

void main() => runApp(const FoodApp());

class FoodApp extends StatelessWidget {
  const FoodApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const FoodPage(),
    );
  }
}

class FoodPage extends StatefulWidget {
  const FoodPage({super.key});

  @override
  State<FoodPage> createState() => _FoodPageState();
}

class _FoodPageState extends State<FoodPage> {
  final items = [
    {"name": "Pizza", "price": 12.0},
    {"name": "Burger", "price": 8.5},
    {"name": "Pasta", "price": 10.0},
  ];

  final cart = <Map<String, dynamic>>[];

  void addItem(Map<String, dynamic> item) => setState(() => cart.add(item));

  @override
  Widget build(BuildContext context) {
    final total = cart.fold<double>(0, (s, item) => s + item["price"]);
    return Scaffold(
      appBar: AppBar(title: const Text("Food Delivery")),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: items.length,
              itemBuilder: (_, i) {
                final item = items[i];
                return Card(
                  margin: const EdgeInsets.all(8),
                  child: ListTile(
                    title: Text(item["name"]),
                    subtitle: Text("\$${item["price"]}"),
                    trailing: ElevatedButton(
                      onPressed: () => addItem(item),
                      child: const Text("Add"),
                    ),
                  ),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16),
            child: Text("Total: \$${total.toStringAsFixed(2)}"),
          )
        ],
      ),
    );
  }
}