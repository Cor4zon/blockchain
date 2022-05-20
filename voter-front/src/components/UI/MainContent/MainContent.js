import React from 'react';
import ActionCard from '../ActionCard/ActionCard';
import { Link } from "react-router-dom";

import "./MainContent.css";

const MainContent = () => {
    return (
        <div className="content">
            <Link to="voting">
                <ActionCard text={"Сгенерировать пару ключей"} />
            </Link>
            <Link to="voter">
                <ActionCard text={"Голосовать"} />
            </Link>
            <Link to="voting_option">
                <ActionCard text={"Посмотреть результаты"} />
            </Link>
        </div>
    );
};

export default MainContent;
