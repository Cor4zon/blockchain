import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";

import VotingForm from './components/UI/VotingForm/VotingForm';
import VoterForm from "./components/UI/VoterForm/VoterForm";
import VotingOptionForm from "./components/UI/VotingOptionForm/VotingOptionForm";

import MainContent from "./components/UI/MainContent/MainContent";
import VotingList from "./components/VotingList/VotingList";
import Voting from "./components/VotingList/Voting/Voting";
import VotingInfo from "./components/VotingList/VotingInfo/VotingInfo";

const root = ReactDOM.createRoot(
    document.getElementById("root")
);

root.render(
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<App />}>
                <Route index path="/" element={<MainContent />} />
                <Route path="voting" element={<Voting />} >
                    <Route index path="" element={<VotingList />} />
                    <Route path=":voting_id" element={<VotingInfo />} />
                </Route>

                <Route path="voter" element={<VoterForm />} />
                <Route path="voting_option" element={<VotingOptionForm />} />
            </Route>
        </Routes>
    </BrowserRouter>
);
