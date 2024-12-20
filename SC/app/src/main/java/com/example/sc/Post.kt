package com.example.sc

data class Post(
    val postId: String? = null,  // 貼文唯一 ID
    val userId: String? = null,  // 使用者 ID
    val username: String? = null,  // 使用者名稱
    val content: String? = null,  // 貼文內容
    val imageUrl: String? = null,  // 貼文圖片URL
    val profileImageUrl: String? = null,  // 使用者頭像URL
    val timestamp: Long? = null,  // 貼文時間戳記
    val imageUrls: List<String>? = null,  // 貼文多張圖片URL
    val subject: String? = null ,// 貼文主題
    var likes: Int = 0,   // 新增愛心數
   // val comments: Map<String, Any>? = null, // 新增留言數
    var isLikedByUser: Boolean = false // 使用者是否已點讚


)
