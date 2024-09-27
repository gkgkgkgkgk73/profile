import React, { useState, useEffect } from 'react';
import Styled from 'styled-components';
import Career from '../components/Career';
import { CareerType } from '../types/CareerType';
import { useLocation } from 'react-router-dom';

interface CareerProps {

    Careers: CareerType[];

}

function CareerList() {
    const location = useLocation();

    const [careers, setCareers] = useState<CareerProps>(location.state?.careers);

    return (
        <CLContainer>
            {careers.Careers.map((c)=>(
                <Career detail={c}/>
            ))}
        </CLContainer>
    );
}

// function CareerList() {
//     return (
//         <CLContainer>
//             <Career />
//         </CLContainer>
//     );
// }

const CLContainer = Styled.div`
    display: flex;
`;

export default CareerList;