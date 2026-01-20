# 🎬 Item-Based Collaborative Filtering Recommendation System

> **A from-scratch, data-structure-driven recommender system built for academic excellence**

---

## 📘 Course Details
- **Course:** Z5007 – Programming and Data Structures  
- **Program:** M.Tech Data Science & Artificial Intelligence  
- **Institute:** Indian Institute of Technology Madras – Zanzibar  
- **Instructor:** Dr. Innocent Nyalala  

---

## 👥 Team Members
- **Surabhi Gudla** (ZDA25M001)  
- **Vineet Joshi** (ZDA25M007)  

---

## ✨ Project Motivation

With the rapid growth of digital platforms such as Netflix, Amazon Prime, and Spotify, users are overwhelmed by the sheer volume of available content.  
Recommendation systems play a critical role in **personalizing user experience** by suggesting relevant items based on historical interactions.

This project aims to **demystify recommendation systems** by building an **Item-Based Collaborative Filtering (IBCF)** engine **entirely from scratch**, emphasizing **core data structures, algorithmic efficiency, and transparency**.

---

## 🎯 Problem Statement

Users often struggle to discover content that matches their preferences due to:
- Large item catalogs  
- Sparse user interactions  
- Lack of explainability in black-box recommender models  

This project addresses these challenges by designing a recommendation system that:
- Learns similarity between items using user ratings  
- Predicts preferences for unseen items  
- Produces fast and accurate Top-N recommendations  

---

## 🧠 Methodology Overview

The system follows an **Item-Based Collaborative Filtering** approach:

- Items (movies) are compared instead of users
- Similar items are identified based on common user ratings
- Recommendations are generated using weighted similarity scores

> **Key Idea:**  
> *If users rate two movies similarly, those movies are considered similar.*

---

## 🏗️ System Architecture

User–Item Ratings
↓
Data Preprocessing
↓
Hash Tables (User→Item, Item→User)
↓
Item–Item Similarity Computation
↓
Rating Prediction Engine
↓
Priority Queue (Top-N Selection)
↓
Final Recommendations


---

## 📁 Project Structure

recommendation_system/
│
├── data/
│ ├── ratings.csv
│ └── movies.csv
│
├── data_loader.py # Data loading & hash table construction
├── similarity.py # Item–item cosine similarity
├── recommender.py # Rating prediction & top-N logic
├── evaluation.py # Precision, Recall, NDCG
├── main.py # End-to-end pipeline
├── Testing_ReccSys.ipynb # Testing & analysis notebook
└── README.md


---

## 📊 Dataset Description

- **Dataset:** MovieLens Latest Small  
- **Source:** GroupLens Research  
- **Size:** ~100,000 ratings  
- **Users:** ~600  
- **Movies:** ~9,000  

**Files Used:**
- `ratings.csv` → userId, movieId, rating, timestamp  
- `movies.csv` → movieId, title, genres  

---

## 🧱 Core Data Structures Used

| Data Structure | Purpose |
|---------------|--------|
| **Hash Tables (dict)** | Constant-time access to user–item data |
| **Graphs (Adjacency Lists)** | Represent item similarity relationships |
| **Priority Queue (Heap)** | Efficient Top-N recommendation retrieval |

---

## 📐 Algorithms Implemented

### 🔹 Item–Item Similarity
- **Metric:** Cosine Similarity
- Computed using overlapping users only
- Top-K neighbors retained for efficiency

### 🔹 Rating Prediction
For user *u* and unseen item *i*:

\[
\hat{r}_{u,i} = \frac{\sum sim(i,j)\cdot r_{u,j}}{\sum |sim(i,j)|}
\]

### 🔹 Top-N Recommendation
- Uses a priority queue (`heapq`)
- Time Complexity: **O(M′ log N)**

---

## 📈 Evaluation Metrics

The system is evaluated using standard recommender-system metrics:

- **Precision@K**
- **Recall@K**
- **NDCG@K**

Evaluation is performed on an **80–20 train-test split** and compared against:
- Random recommendation baseline  
- Popularity-based baseline  

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install numpy pandas matplotlib

python main.py

3️⃣ Notebook (Optional)

Open Testing_ReccSys.ipynb to inspect:

Intermediate outputs

Similarity matrices

Evaluation results

✅ Key Highlights

✔ Built entirely from scratch
✔ No black-box recommender libraries
✔ Strong focus on data structures & algorithms
✔ Efficient (< 1 second per user)
✔ Fully aligned with academic learning objectives

🔮 Future Enhancements

Content-based or hybrid recommendation

Scalability to large datasets

Web-based user interface

📚 References

Sarwar et al., Item-Based Collaborative Filtering Recommendation Algorithms

Herlocker et al., Evaluating Collaborative Filtering Recommender Systems

🏁 Conclusion

This project demonstrates how a real-world recommendation system can be built using fundamental programming concepts and data structures, providing both practical relevance and academic rigor.
It serves as a strong foundation for further exploration in recommender systems and applied machine learning.


---

### 💡 Tip for GitHub
**Repository description (one-liner):**
> *Item-Based Collaborative Filtering recommender system implemented from scratch using core data structures and algorithms.*

---

If you want, I can now:
- Add **badges** (Python, MIT License, IIT)
- Make a **1-page project poster**
- Convert this into **final report text**
- Prepare **viva Q&A from this README**

Just tell me 👍
