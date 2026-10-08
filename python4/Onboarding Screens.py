import 'package:flutter/material.dart';

void main() => runApp(const OnboardingApp());

class OnboardingApp extends StatelessWidget {
  const OnboardingApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const OnboardingPage(),
    );
  }
}

class OnboardingPage extends StatefulWidget {
  const OnboardingPage({super.key});

  @override
  State<OnboardingPage> createState() => _OnboardingPageState();
}

class _OnboardingPageState extends State<OnboardingPage> {
  final controller = PageController();
  int index = 0;

  final pages = const [
    {"title": "Welcome", "text": "Start your journey."},
    {"title": "Learn", "text": "Build projects step by step."},
    {"title": "Grow", "text": "Create apps with confidence."},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView.builder(
        controller: controller,
        onPageChanged: (i) => setState(() => index = i),
        itemCount: pages.length,
        itemBuilder: (_, i) {
          final p = pages[i];
          return Center(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(p["title"]!, style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 12),
                  Text(p["text"]!, style: const TextStyle(fontSize: 18)),
                ],
              ),
            ),
          );
        },
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.all(16),
        child: ElevatedButton(
          onPressed: () {
            if (index < pages.length - 1) {
              controller.nextPage(duration: const Duration(milliseconds: 300), curve: Curves.easeInOut);
            }
          },
          child: Text(index == pages.length - 1 ? "Done" : "Next"),
        ),
      ),
    );
  }
}