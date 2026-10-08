import 'package:flutter/material.dart';

void main() => runApp(const ProductApp());

class ProductApp extends StatelessWidget {
  const ProductApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text("Product")),
        body: const Padding(
          padding: EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Placeholder(fallbackHeight: 200),
              SizedBox(height: 16),
              Text("Product Name", style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
              Text("\$99.99", style: TextStyle(fontSize: 22)),
              SizedBox(height: 12),
              Text("This is a sample product details page."),
            ],
          ),
        ),
      ),
    );
  }
}