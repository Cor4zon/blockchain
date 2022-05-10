import React, { useState, useEffect } from 'react';

import APIClient from "../../services/APIClient";
import VotingCard from './VotingCard/VotingCard'
import VotingForm from "../UI/VotingForm/VotingForm";

const VotingList = () => {
    const [ votings, setVotings ] = useState([]);
    const client = new APIClient();

    useEffect(() => {
        client.fetchVotings().then((result) => {
            setVotings(result.data)
        });
    }, [votings]);

    return (
        <div>
            { votings.map(voting => {
                return <VotingCard key={voting.id} voting={voting} />
            }) }

            <VotingForm />
        </div>
    );
};

export default VotingList;
