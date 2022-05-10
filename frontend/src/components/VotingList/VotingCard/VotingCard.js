import React from 'react';
import { Link } from "react-router-dom";

const VotingCard = ({ voting }) => {

    return (
        <div>
            <Link to={`${voting.id}`} >
                <h3> { voting.title } </h3>
            </Link>
            <p> { voting.description } </p>
            <p> { voting.deadline } </p>
        </div>
    );
};

export default VotingCard;
