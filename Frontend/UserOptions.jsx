import React,{useState} from "react";
import { useNavigate } from "react-router";
import "./childComponents.css";

const UserOptions = () => {

    const navigate = useNavigate();

    return (
        <>
        <button className="register-option" onClick={(e) => navigate("/register/")}>Register</button>
        <button className="login-option" onClick={(e) => navigate("/login/")}>Login</button>
        </>
    )
    
}

export default UserOptions;