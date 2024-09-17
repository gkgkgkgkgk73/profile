import React, { useState } from 'react';
import Styled from 'styled-components';
import Career from '../components/Career';
import { CareerType } from '../types/CareerType';

interface CareerProps {

    Careers: CareerType[];

}

// function CareerList(careers: CareerProps) {
//     return (
//         <CLContainer>
//             <Career />
//         </CLContainer>
//     );
// }

function CareerList() {
    return (
        <CLContainer>
            <Career />
        </CLContainer>
    );
}

const CLContainer = Styled.div`
    display: flex;
`;

export default CareerList;