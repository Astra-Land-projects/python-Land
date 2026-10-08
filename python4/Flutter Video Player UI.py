import 'package:flutter/material.dart';

void main() {
  runApp(const VideoApp());
}

class VideoApp extends StatelessWidget {
  const VideoApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Video Player',
      theme: ThemeData(
        useMaterial3: true,
      ),
      home: const VideoPage(),
    );
  }
}

class VideoPage extends StatelessWidget {
  const VideoPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:
            const Text('Video Player'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment:
              MainAxisAlignment.center,
          children: [
            Container(
              width: double.infinity,
              height: 220,
              margin:
                  const EdgeInsets.all(16),
              color: Colors.black,
              child: const Center(
                child: Icon(
                  Icons.play_circle,
                  color: Colors.white,
                  size: 80,
                ),
              ),
            ),
            const Text(
              'My Video',
              style: TextStyle(
                fontSize: 24,
                fontWeight:
                    FontWeight.bold,
              ),
            ),
            Slider(
              value: 0.3,
              onChanged: (_) {},
            ),
          ],
        ),
      ),
    );
  }
}