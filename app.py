import streamlit as st
import time
import os

# 페이지 기본 설정
st.set_page_config(
    page_title="광양 서천 수질 오염의 심각성",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 1. 사이트 처음 페이지 (제목 글귀 및 배경 이미지) ---

# 이미지 폴더 경로 설정
image_dir = 'images'
if not os.path.exists(image_dir):
    st.error(f"'{image_dir}' 폴더를 찾을 수 없습니다. 서천 배경 이미지를 넣어주세요.")
    st.stop()

# 이미지 파일 목록 가져오기 (확장자 고려)
background_images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

if not background_images:
    st.error(f"'{image_dir}' 폴더에 이미지가 없습니다. 이미지를 넣어주세요.")
    st.stop()

# 이미지 순환을 위한 세션 상태 초기화
if 'current_bg_index' not in st.session_state:
    st.session_state.current_bg_index = 0

# 배경 이미지 표시 (전체 너비 사용)
# 이미지를 중앙에 배치하고 높이를 조절하기 위해 CSS 활용
st.markdown("""
<style>
    .stApp {
        background-size: cover;
        background-position: center;
        transition: background-image 1s ease-in-out;
    }
    .main-title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh; /* 화면 높이의 80%를 차지하도록 설정 */
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        padding: 20px;
        box-sizing: border-box;
    }
    .main-title {
        font-size: 3.5em; /* 글자 크기 조정 */
        font-weight: bold;
    }
    /* 스크롤 다운 아이콘 스타일 */
    .scroll-down-arrow {
        position: absolute;
        bottom: 50px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 3em;
        color: white;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-30px);
        }
        60% {
            transform: translateY(-15px);
        }
    }
</style>
""", unsafe_allow_html=True)

# 현재 배경 이미지 경로 가져오기
current_bg_image = background_images[st.session_state.current_bg_index]

# CSS를 사용하여 배경 이미지 설정
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{open(current_bg_image, "rb").read().__str__()}");
        background-attachment: fixed; /* 스크롤 시 배경 고정 */
    }}
</style>
""", unsafe_allow_html=True)

# 메인 타이틀 표시
st.markdown("""
<div class="main-title-container">
    <h1 class="main-title">깨끗한 서천, 우리가 나서지 않으면 누가 지킬 수 있을까요?</h1>
</div>
<div class="scroll-down-arrow">
    &#x2193; </div>
""", unsafe_allow_html=True)


# 이미지 순환 로직 (옵션: 자동 순환)
# st.experimental_rerun()을 사용하면 페이지가 새로고침되므로,
# 배경 이미지만 부드럽게 전환하려면 JavaScript를 사용해야 하지만, Streamlit에서는 직접적인 JS 제어가 제한적입니다.
# 여기서는 간단하게 Streamlit의 rerun 기능을 활용하여 이미지를 변경하지만,
# 실제로 부드러운 전환을 원한다면 프론트엔드 기술(React, Vue 등)을 함께 사용하는 것이 좋습니다.
# for _ in range(len(background_images)):
#     st.session_state.current_bg_index = (st.session_state.current_bg_index + 1) % len(background_images)
#     time.sleep(5) # 5초마다 이미지 변경
#     st.experimental_rerun()


# 다음 이미지로 인덱스 업데이트 (수동 또는 자동 스크롤 시)
# 웹사이트 방문자가 스크롤을 내리면 다음 섹션이 보이므로,
# 배경 이미지를 계속 순환시킬 필요는 없습니다. 첫 페이지에만 적용합니다.


# --- 2. 소개글 ---

# 첫 화면과 소개글 사이의 간격 추가 (시각적 구분)
st.markdown("<div style='height: 100vh;'></div>", unsafe_allow_html=True) # 첫 페이지 높이만큼 스크롤을 내려야 소개글이 보이도록 설정

st.markdown("## 소개", unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 1.2em; line-height: 1.6;">
서천은 지역 주민들과 생물들에게 소중한 쉼터이자 생명의 터전입니다. 그러나 최근 무단 투기된 쓰레기들로 인해 하천 미관이 심각하게 훼손되고, 수질 악화 및 생태계 파괴 문제가 날로 심각해지고 있습니다.
<br><br>
이 웹사이트는 이러한 환경 문제를 알리고, 지역 사회와 함께 서천을 보호하기 위한 다양한 홍보, 캠페인, 자원봉사 활동을 연결하기 위해 만들어졌습니다.
<br><br>
쓰레기 하나 줄이기, 함께 정화 활동 참여하기, 주변에 문제를 알리기—당신의 관심과 실천이 서천을 다시 되살릴 수 있습니다.
<br><br>
자연은 말하지 않지만, 우리는 행동할 수 있습니다.
</div>
""", unsafe_allow_html=True)

# 하단 여백 추가
st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)
# --- 3. 정보 섹션 시작 ---
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True) # 소개글과 정보 섹션 사이 간격
st.markdown("---")
st.markdown("<h2 style='text-align: center; font-size: 2.5em; margin-bottom: 40px; color: #333;'>서천 수질 오염 문제의 심각성</h2>", unsafe_allow_html=True)

# 3.1. 서천 수질 오염 현황
st.markdown("<h3 style='color: #333;'>3.1. 서천 수질 오염 현황</h3>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #f0f2f6; padding: 25px; border-radius: 10px; margin-bottom: 30px; color: #333;">
    <p style="font-size: 1.1em; line-height: 1.6;">
    광양 서천은 한때 맑은 물과 풍부한 생태계를 자랑하던 곳이었지만, 무분별한 쓰레기 투기와 생활 하수 유입으로 인해 그 아름다움을 잃어가고 있습니다. 특히, <strong>수질 검사 결과 부유 물질 및 특정 오염 물질 농도가 급증</strong>하고 있으며, 이는 하천 바닥의 퇴적물 증가와 생물의 서식지 파괴로 이어지고 있습니다.
    </p>
    <p style="font-size: 1.1em; line-height: 1.6;">
    주민들의 제보와 현장 조사에 따르면, 플라스틱 병, 스티로폼, 비닐 등 장기간 분해되지 않는 쓰레기들이 하천 곳곳에 쌓여 미관을 해치는 것은 물론, 빗물과 함께 강으로 유입되어 <strong>더 큰 해양 오염</strong>으로 이어질 가능성이 큽니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 여기에 현황 관련 이미지나 그래프를 추가할 수 있습니다.
# 예: st.image("path/to/pollution_image1.jpg", caption="서천에 버려진 쓰레기들")

# 3.2. 수질 오염의 문제점
st.markdown("<h3 style='color: #333;'>3.2. 수질 오염의 문제점</h3>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #f0f2f6; padding: 25px; border: 1px solid #e0e0e0; border-radius: 10px; margin-bottom: 30px; color: #333;">
    <ul style="font-size: 1.1em; line-height: 1.8;">
        <li><strong>생태계 파괴:</strong> 오염된 물은 어류, 수생 식물, 곤충 등 수많은 생명체의 생존을 위협하며, 이는 먹이 사슬 전반에 악영향을 미쳐 생물 다양성을 감소시킵니다.</li>
        <li><strong>미관 훼손 및 악취:</strong> 쌓인 쓰레기와 오염된 물은 하천 주변의 경관을 해치고 불쾌한 악취를 유발하여 주민들의 삶의 질을 저하시킵니다.</li>
        <li><strong>질병 유발 가능성:</strong> 오염된 물은 박테리아, 바이러스 등 유해 물질을 퍼뜨려 사람과 동물의 건강에 직접적인 위협이 될 수 있습니다.</li>
        <li><strong>지속 가능한 발전 저해:</strong> 건강한 하천은 지역 사회의 중요한 자원이지만, 오염으로 인해 관광, 레저 활동 등 지역 발전 가능성이 줄어듭니다.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 3.3. 해결 방안 및 우리의 역할
st.markdown("<h3 style='color: #333;'>3.3. 해결 방안 및 우리의 역할</h3>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #e6f7ff; padding: 25px; border-radius: 10px; margin-bottom: 30px; color: #333;">
    <p style="font-size: 1.1em; line-height: 1.6;">
    서천의 오염 문제를 해결하기 위해서는 우리 모두의 관심과 적극적인 참여가 필요합니다.
    </p>
    <ul style="font-size: 1.1em; line-height: 1.8;">
        <li><strong>쓰레기 무단 투기 근절:</strong> 쓰레기는 반드시 지정된 장소에 올바르게 분리하여 배출합시다.</li>
        <li><strong>정화 활동 참여:</strong> 지역 사회에서 진행되는 하천 정화 활동에 자원봉사자로 참여하여 직접 환경 보호에 기여할 수 있습니다.</li>
        <li><strong>환경 보호 캠페인 확산:</strong> 가족, 친구, 이웃들에게 서천의 문제를 알리고 환경 보호의 중요성을 공유합시다.</li>
        <li><strong>지속 가능한 소비 습관:</strong> 일회용품 사용을 줄이고 재활용을 생활화하여 환경에 대한 부담을 줄이는 노력을 합니다.</li>
    </ul>
    <p style="font-size: 1.1em; line-height: 1.6; margin-top: 20px; font-weight: bold;">
    작은 실천들이 모여 깨끗한 서천을 되찾을 수 있습니다. 지금 바로 행동해주세요!
    </p>
</div>
""", unsafe_allow_html=True)

# --- 정보 섹션 끝 ---

# 하단 여백 추가
st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)
# --- 4. 봉사 신청 섹션 시작 ---
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div class='volunteer-section'>
    <h2>봉사 신청</h2>
    <p>
    서천을 깨끗하게 만드는 일에 동참하고 싶으신가요? 여러분의 작은 관심과 행동이 서천의 내일을 바꿀 수 있습니다. 
    아래 버튼을 클릭하여 1365 자원봉사 포털에서 광양 서천 관련 봉사 활동을 찾아보세요!
    </p>
    """, unsafe_allow_html=True)

# 1365 자원봉사 사이트로 연결되는 버튼
# st.link_button은 클릭 시 새 탭으로 링크를 엽니다.
st.link_button(
    "1365 자원봉사 사이트 바로가기",
    url="https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do",
    help="새 탭에서 1365 자원봉사 포털로 이동합니다."
)

st.markdown("""
    <p style="font-size: 0.9em; margin-top: 20px; opacity: 0.8;">
    * 1365 사이트 접속 후, '전남 광양시'를 검색하시면 서천 관련 봉사 활동을 찾으실 수 있습니다.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 봉사 신청 섹션 끝 ---

# 하단 여백 추가
st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)
