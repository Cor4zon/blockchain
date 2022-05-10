import React from 'react';
import ActionCard from '../ActionCard/ActionCard';
import { Link } from "react-router-dom";

import "./MainContent.css";

const MainContent = () => {
    return (
        <div className="content">
            <Link to="voting">
                <ActionCard text={"Создать голосование"} />
            </Link>
            <Link to="voter">
                <ActionCard text={"Добавить кандидатов"} />
            </Link>
            <Link to="voting_option">
                <ActionCard text={"Добавить голосующих"} />
            </Link>
        </div>
    );
};

export default MainContent;
