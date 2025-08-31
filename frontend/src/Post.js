import React, {useState, useEffect} from "react";
import './Post.css'
import { Button, Avatar } from "@mui/material";
// import Avatar from "@mui/material/Avatar";


const BASEURL = 'http://127.0.0.1:8000/'

function Post({post, username, authToken, authTokenType}){

    const [imageUrl, setImageUrl] = useState('')
    const [comments, setComment] = useState([])
    const [newComment, setNewComment] = useState('')

    // const [authToken, setAuthToken] = useState("")

    useEffect(()=> {
        if (post.image_url_type === 'absolute'){
                setImageUrl(post.image_url)
            }
        else{
            setImageUrl(BASEURL + post.image_url)
        }
    }, [post]);

    useEffect(()=>{
        setComment(post.comments)
    }, [post])

    const handleComment = (event) => {
        event?.preventDefault()

        const json_string = JSON.stringify({
            'username': username,
            'text': newComment,
            'post_id': post.id,
            'likes':0,
        })

        const requestOptions = {
            method: "POST",
            headers: new Headers({
                //"Authentication": authTokenType + ' ' + authToken,
                "Authorization": authTokenType + " " + authToken, 
                "Content-Type": 'application/json',
            }),
            body: json_string,
        }

        fetch(BASEURL + 'post/new-comment', requestOptions)
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
        fetch(BASEURL + 'post/all-comment/' + post.id)
        .then(response => {
            if (response.ok){
                return response.json()
            }
            throw response
        })
        .then(data => {
            console.log("setComment", data)
            setComment(data)
        })
        .catch(error => {
            console.log(error);
        })
    }


    const handleDelete = (event) => {
        event?.preventDefault()

        const requestOptions = {
            method: 'DELETE',
            headers: new Headers({
                "Authorization" : authTokenType + ' ' + authToken
            })
        }

        fetch(BASEURL + 'post/delete/' + post.id, requestOptions)
        .then(response => {
            if (response.ok){
                window.location.reload()
            }
            throw response
        })
        .catch(error => {
            console.error(error)
        })
    }


    return (
        <div className="post">
            <div className="post_header">

                <Avatar
                    alt="{post.username}"
                    src={imageUrl}
                />
                <div className="post_header_info">
                    <h3>{post.user.username}</h3>
                    <Button className="post_delete" onClick={handleDelete}>Delete</Button>
                </div>
                
            </div>
            <div className="post_title">
                <h5> {post.post_title} </h5>
            </div>
            
            <img 
            className="post_img" 
            src={imageUrl}
            alt=""
            />

            <h4 className="post_caption"> {post.caption} </h4>
            <div className="post_comment"> 
                {/* { 
                comments.map((comment) => (
                    <p>
                        <strong> {comment.username} : </strong> {comment.text}
                    </p>
                )) 
                } */}

                {comments.length > 0 ? (
                    comments.map((comment) => (
                        <p key={comment.id}>
                            <strong>{comment.username}:</strong> {comment.text}
                        </p>
                    ))
                    ) : (
                        <p>No comments yet.</p>
                )}
            </div>
            

            { authToken ? 
                (
                    <form className="comment_form">
                        <input type="text" 
                        className="comment_input"
                        placeholder="Add a comment"
                        value={newComment}
                        onChange={(e) => setNewComment(e.target.value)}
                        />
                        <button 
                        type="Submit"
                        className="comment_button"
                        disabled={!newComment}
                        onClick={handleComment}
                        >
                           Post
                        </button>
                    </form>
                ) : (
                    <div className=""></div>
                )
            
            }

        </div>
    )
}

export default Post