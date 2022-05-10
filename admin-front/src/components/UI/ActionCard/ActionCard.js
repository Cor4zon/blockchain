import React from 'react';

import "./ActionCard.css";

const ActionCard = ({ text }) => {
    return (
        <div className="action_card">
            <p> { text } </p>
        </div>

    );
};

export default ActionCard;
