import 'package:flutter/material.dart';

void main() => runApp(const CartApp());

class CartApp extends StatelessWidget {
  const CartApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const CartPage(),
    );
  }
}

class CartPage extends StatefulWidget {
  const CartPage({super.key});

  @override
  State<CartPage> createState() => _CartPageState();
}

class _CartPageState extends State<CartPage> {
  final items = <Map<String, dynamic>>[
    {"name": "Laptop", "price": 999.0},
    {"name": "Mouse", "price": 25.0},
  ];

  @override
  Widget build(BuildContext context) {
    final total = items.fold<double>(0, (s, item) => s + item["price"]);
    return Scaffold(
      appBar: AppBar(title: const Text("Cart")),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: items.length,
              itemBuilder: (_, i) => ListTile(
                title: Text(items[i]["name"]),
                trailing: Text("\$${items[i]["price"]}"),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16),
            child: Text("Total: \$${total.toStringAsFixed(2)}"),
          ),
        ],
      ),
    );
  }
}