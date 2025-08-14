import React,{useState} from "react";
import { useNavigate } from "react-router";
import image from "./../../images/tl.png";
import image1 from "./../../images/Kids-Sport-PNG-Pic.png"
import image2 from "./../../images/3447513.png"
const HomePage = ({}) => {
    
    const navigate = useNavigate();

    return (
        <>
            {/* Container for the About Me button */}
            <div className="top-left-buttons">
                <button className="about-me-home-page-signed-out" onClick={(e) => navigate("/about-me")}>
                    About Me
                </button>
            </div>
    
            {/* Container for the Join Now and Log In buttons */}
            <div className="top-right-buttons">
                <button className="register-option" onClick={(e) => navigate("/register/")}>
                    Join Now
                </button>
                <button className="login-option" onClick={(e) => navigate("/login/")}>
                    Log In
                </button>
            </div>
    
            {/* Rest of the page content */}
            <div>
                <img src={image} alt="Three people from a cartoon"></img>
                <h1 className="find-community-home-page-signed-out">Find Your Community</h1>
                <img src={image1} alt="A group of 5 people connecting through different sports"></img>
                <h1 className="friend-suggestions-home-page-signed-out">Get Friend Suggestions based on shared hobbies</h1>
                <p>
                    <button className="basketball-home-page-button">Watching Basketball</button>
                    <button className="traveling-home-page-button">Traveling</button>
                    <button className="photography-home-page-button">Photography</button>
                    <button className="chess-home-page-button">Chess</button>
                    <button className="coding-home-page-button">Coding</button>
                    <button className="food-home-page-button">New Food</button>
                </p>
                <h1>👍 👎</h1>
                <h1 className="accept-reject-home-page-signed-out">Accept or Reject Friend Requests</h1>
                <img src={image2} alt="Two text bubbles"></img>
                <h1 className="message-people-home-page-signed-out">Message People in Real-Time</h1>
            </div>
        </>
    )
}
export default HomePage;