import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes} from "react-router-dom";

import App from './App';
import MainContent from "./components/UI/MainContent/MainContent";
import CreateKeys from "./components/CreateKeys";

const root = ReactDOM.createRoot(
    document.getElementById("root")
);

root.render(
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<App />}>
                <Route index path="/" element={<MainContent />} />
                {/*<Route path="voting" element={<Voting />} >*/}
                {/*    <Route index path="" element={<VotingList />} />*/}
                {/*    <Route path=":voting_id" element={<VotingInfo />} />*/}
                {/*</Route>*/}

                <Route path="create_keys" element={<CreateKeys />} />
            </Route>
        </Routes>
    </BrowserRouter>
);
