import React, { useState } from 'react';
import Styled from 'styled-components';
import { CareerType } from '../types/CareerType';

interface CareerDetail {
    detail: CareerType;
}
// 경력사항
function Career(career: CareerDetail) {
    return (
        <CContainer>
            <CName>{career.detail.name}</CName>
            <CPeriod>{career.detail.period}</CPeriod>
            <CRole>{career.detail.role}</CRole>
            {career.detail.description.map((str)=> (
                <CDescription>
                    | {str}
                </CDescription>
            ))}
        </CContainer>
    );
}

// const descriptionex = [
//     "Riot 사의 ‘전략적 팀 전투’ 게임 분석 사이트 기획/개발",
//     "React, Django를 사용하여 게임 분석 내용을 볼 수 있는 웹사이트 기획/개발",
//     "같은 UI를 유지하기 위해 Component를 만들어 최대한 활용, 동적인 움직임을 위해 Styled-Component 활용"  
// ];

// function Career() {
//     return (
//         <CContainer>
//             <CName>TFTInfo</CName>
//             <CPeriod>2023.01 ~</CPeriod>
//             <CRole>| Frontend Developer, Backend Developer</CRole>
//             {descriptionex.map((str)=> (
//                 <CDescription>
//                     º {str}
//                 </CDescription>
//             ))}
//         </CContainer>
//     );
// }


// styled-components 사용
const CContainer = Styled.div`

`
;

const CName = Styled.p`
    font-family: KakaoBold;
    font-size: 10rem;
    color: black;
`;

const CPeriod = Styled.p`
    font-family: KakaoBold;
    font-size: 6rem;
    color: grey;
`;

const CRole = Styled.p`
    font-family: KakaoBold;
    font-size: 8rem;
    color: grey;
`;

const CDescription = Styled.p`
    font-family: KakaoRegular;
    font-size: 8rem;
    color: black;
    margin-left: 20px;
`;

export default Career;