import React from 'react';
import { Outlet } from "react-router-dom";

import VotingCard from "../VotingCard/VotingCard";

const Voting = ({ voting }) => {

    return (
        <div>
            <Outlet />
        </div>
    );
};

export default Voting;
