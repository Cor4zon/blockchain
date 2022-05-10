import React from 'react';
import { Outlet } from "react-router-dom";

import MainContent from "./components/UI/MainContent/MainContent";
import VotingForm from "./components/UI/VotingForm/VotingForm";

const App = () => {
    return (
        <div>
           <h1>Blockchain voting</h1>
            <Outlet />

        </div>
    );
};

export default App;