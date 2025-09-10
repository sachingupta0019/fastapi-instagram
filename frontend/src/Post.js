import React, {useState, useEffect} from "react";
import './Post.css'
import { Avatar, Button } from "@mui/material";

// const BASE_URL = 'http://localhost:8000/'
const BASE_URL = "https://fastapi-instagram.onrender.com/";
// const BASE_URL = process.env.REACT_APP_BASE_URL;


function Post({ post, authToken, authTokenType, username }) {

  const [imageUrl, setImageUrl] = useState('')
  const [comments, setComments] = useState([])
  const [newComment, setNewComment] = useState('')

  useEffect(() => {
    if (post.image_url_type === 'absolute') {
      setImageUrl(post.image_url)
    } else {
      // setImageUrl(`${BASE_URL}${post.image_url}`)
      setImageUrl(`${BASE_URL.replace(/\/$/, '')}/${post.image_url.replace(/^\//, '')}`);

    }
  }, [post])

  useEffect(() => {
    setComments(post.comments)
  }, [post])

  const handleDelete = (event) => {
    event?.preventDefault();

    const requestOptions = {
      method: 'DELETE',
      headers: new Headers({
        'Authorization': authTokenType + ' ' + authToken
      })
    }

    fetch(BASE_URL + 'post/delete/' + post.id, requestOptions)
      .then(response => {
        if (response.ok) {
          window.location.reload()
        }
        throw response
      })
      .catch(error => {
        console.log(error);
      })
  }


  const postComment = (event) => {
    event?.preventDefault()

    const json_string = JSON.stringify({
      'username': username,
      'text': newComment,
      'likes': 0,
      'post_id': post.id
    })

    const requestOptions = {
      method: 'POST',
      headers: new Headers({
        'Authorization': authTokenType + ' ' + authToken,
        'Content-Type': 'application/json'
      }),
      body: json_string
    }

    fetch(BASE_URL + 'post/new-comment', requestOptions)
      .then(response => {
        if (response.ok) {
          return response.json()
        }
      })
      .then(data => {
        fetchComments()
      })
      .catch(error => {
        console.log(error);
      })
      .finally(() => {
        setNewComment('')
      })
  }

  const fetchComments = () => {
    fetch(BASE_URL + 'post/all-comment/' + post.id)
      .then(response => {
        if (response.ok) {
          return response.json()
        }
        throw response
      })
      .then(data => {
        setComments(data)
      })
      .catch(error => {
        console.log(error);
      })
  }

  return (
    <div className="post">
      <div className="post_header">
        <Avatar
          alt=""
          src={imageUrl}
        />
        <div className="post_headerInfo">
          <h3>{post.user.username}</h3>
          <Button className="post_delete" onClick={handleDelete}>
            Delete
          </Button>
        </div>
      </div>

      <img
        className="post_img"
        src={`${BASE_URL}/images/${post.image}`}
        
        alt=""
      />

      <h4 className='post_text'>{post.caption}</h4>

      <div className='post_comments'>
        {
          comments.map((comment) => (
            <p>
              <strong>{comment.username}:</strong> {comment.text}
            </p>
          ))
        }
      </div>

      {authToken && (
        <form className="post_commentbox">
          <input className="post_input"
            type="text"
            placeholder="Add a comment"
            value={newComment}
            onChange={(e) => setNewComment(e.target.value)}
          />
          <button
            className="post_button"
            type="submit"
            disabled={!newComment}
            onClick={postComment}>
              Post
            </button>
        </form>
      )}
    </div>
  )
}

export default Post