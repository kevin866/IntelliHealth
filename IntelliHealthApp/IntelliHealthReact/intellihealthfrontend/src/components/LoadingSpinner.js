import React from "react";
import "../styles/Spinner.css";

export default function LoadingSpinner() {
  return (
    // <div className="spinner-container">
    //   <div className="loading-spinner"></div>
    // </div>
    <div className="loader-container">
        <div class="loader-inner">
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
        </div>
    </div>
  );
}