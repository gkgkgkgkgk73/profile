import React, { useState, useEffect } from 'react';
import Styled from 'styled-components';
import Career from '../components/Career';
import { CareerType } from '../types/CareerType';
import { useLocation } from 'react-router-dom';

interface IntroductionProps {

    Introduction: IntroductionType[];

}

function Introduction() {
    const location = useLocation();

    const [intro, setIntro] = useState<IntroductionProps>(location.state?.careers);

    return (
        <IntroContainer>

        </IntroContainer>
    );
}

// function CareerList() {
//     return (
//         <CLContainer>
//             <Career />
//         </CLContainer>
//     );
// }

const IntroContainer = Styled.div`
    display: flex;
`;

export default Introduction;