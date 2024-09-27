import React, { useState } from 'react';
import { PacmanLoader } from 'react-spinners';

const override = {
    span: '20px',
    margin: '0 auto',
    marginTop:'220px',
    color : '#fff',
    size : '20'
};

function Loading() {
    return (
        <PacmanLoader 
        color = '#fff'
        loading = {true}
        cssOverride = {override}
        size = {25}
        speedMultiplier = {0.8}
        margin = {5}
        />
    );
}

export default Loading;