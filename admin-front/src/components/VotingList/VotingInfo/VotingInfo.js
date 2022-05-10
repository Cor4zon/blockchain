import React, { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";

import APIClient from "../../../services/APIClient";
import VotingCard from "../VotingCard/VotingCard";
import VoterForm from "../../UI/VoterForm/VoterForm";
import VotingOptionForm from "../../UI/VotingOptionForm/VotingOptionForm";

const VotingInfo = () => {
    let params = useParams();
    const [ voting, setVoting ] = useState({});

    const client = new APIClient();

    useEffect(() => {
        client.fetchVotings().then((result) => {
            const votings = result.data;
            const voting = votings.filter(item => item.id === +params.voting_id);
            setVoting(voting[0])
        });
    }, [voting]);

    return (
        <div>
            <VotingCard voting={voting} />

            <p>Добавить кандидата</p>
            <VotingOptionForm voting={+params.voting_id} />

            <p>Добавить избирателя</p>
            <VoterForm voting={+params.voting_id} />

        </div>
    );
};

export default VotingInfo;
