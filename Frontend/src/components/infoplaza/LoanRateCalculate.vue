<template>
  <aside class="col-lg-5" style="margin-top: -6rem">
    <div class="sticky-top" style="padding-top: 6rem">
      <div class="card shadow-sm mb-3 mb-lg-0">
        <div class="card-body">
          <h3>대출 계산기</h3>
          <p>이 상품에 대한 대출 금액과 이자를 계산하세요!</p>
          <div class="btn-group" role="group" aria-label="Basic example">
            <button
              type="button"
              class="btn btn-custom"
              :class="{ active: activeButton === 'left' }"
              @click="setActiveButton('left')"
            >
              원리금균등
            </button>
            <button
              type="button"
              class="btn btn-custom"
              :class="{ active: activeButton === 'middle' }"
              @click="setActiveButton('middle')"
            >
              원금균등
            </button>
            <button
              type="button"
              class="btn btn-custom"
              :class="{ active: activeButton === 'right' }"
              @click="setActiveButton('right')"
            >
              만기일시
            </button>
          </div>
          <form @submit.prevent="calculate">
            <div class="form-group">
              <label for="loanAmount">대출금액</label>
              <div class="input-group mb-3">
                <input
                  type="text"
                  class="form-control"
                  id="loanAmount"
                  placeholder="대출금액을 입력하세요"
                  aria-label="대출금액"
                  v-model="formattedLoanAmount"
                  @input="formatCurrency"
                  required
                />
                <div class="input-group-append">
                  <span class="input-group-text">₩</span>
                </div>
              </div>
            </div>
            <div class="form-group">
              <label for="loanTerm">대출 기간</label>
              <div class="input-group mb-3">
                <input
                  type="number"
                  class="form-control"
                  id="loanTerm"
                  placeholder="대출 기간을 입력하세요"
                  v-model="loanTerm"
                  required
                />
                <span class="input-group-text">개월</span>
              </div>
            </div>
            <div class="d-flex justify-content-end">
              <button type="submit" class="btn btn-primary mt-2">
                계산하기
              </button>
            </div>
          </form>
          <hr class="my-4" />
          <div class="d-flex align-items-end">
            <div v-if="monthlyPayment || totalInterest" class="result">
              <p>월 상환액: {{ monthlyPayment.toFixed(0) }}원</p>
              <p>총 이자액: {{ totalInterest.toFixed(0) }}원</p>
            </div>
            <a
              class="btn btn-icon btn-translucent-primary btn-xs rounded-circle"
              href="#"
              ><i class="fi-telegram"></i
            ></a>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const props = defineProps({
  crdtGradAvg: {
    type: Number,
    required: true, // 필수 값
  },
  endpoint: {
    type: String,
    required: true, // 필수 값
  },
  defaultActiveButton: {
    type: String,
    default: 'left', // 기본값을 'left'로 설정
  },
});

const activeButton = ref(props.defaultActiveButton); // props로 활성화된 버튼 처리
const formattedLoanAmount = ref(''); // 대출 금액
const loanTerm = ref(''); // 대출 기간
const monthlyPayment = ref(0); // 월 상환액
const totalInterest = ref(0); // 총 이자액

const setActiveButton = (button) => {
  activeButton.value = button; // 클릭한 버튼을 활성화 상태로 설정
};

// 대출 금액을 화폐 형식으로 변환하는 함수
const formatCurrency = () => {
  let value = formattedLoanAmount.value.replace(/[^0-9]/g, '');
  if (value) {
    value = parseInt(value).toLocaleString();
  }
  formattedLoanAmount.value = value;
};

// 대출 계산 함수
const calculate = () => {
  const rawLoanAmount = parseInt(formattedLoanAmount.value.replace(/,/g, ''));
  const termMonths = parseInt(loanTerm.value);
  const interestRate = props.crdtGradAvg / 100; // 연 이자율
  let monthlyInterestRate = interestRate / 12;

  if (activeButton.value === 'left') {
    // 원리금균등상환
    monthlyPayment.value =
      (rawLoanAmount * monthlyInterestRate) /
      (1 - Math.pow(1 + monthlyInterestRate, -termMonths));
    totalInterest.value = monthlyPayment.value * termMonths - rawLoanAmount;
  } else if (activeButton.value === 'middle') {
    // 원금균등상환
    const principalPayment = rawLoanAmount / termMonths;
    monthlyPayment.value =
      principalPayment +
      (rawLoanAmount -
        principalPayment * Math.floor((termMonths - 1) / termMonths)) *
        monthlyInterestRate;
    totalInterest.value = monthlyPayment.value * termMonths - rawLoanAmount; // 적절한 이자 계산이 필요
  } else if (activeButton.value === 'right') {
    // 만기일시상환
    totalInterest.value = rawLoanAmount * interestRate; // 만기일시상환의 경우 전체 이자
    monthlyPayment.value = 0; // 만기일시상환은 만기일까지 월 상환액이 없음
  }
};

const route = useRoute();
const id = ref(route.params.id); // 라우트에서 ID 가져오기
const BASEURI = '/api/infoPlaza/loan';
const data = ref(); // 상품 데이터

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + props.endpoint, {
      params: {
        id: id.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      data.value = response.data;
      console.log(data.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 페이지가 로드될 때 데이터 가져오기
onMounted(async () => {
  await bringDataList(); // 데이터 가져오기
});
</script>

<style scoped>
.btn-group {
  display: flex;
  justify-content: center; /* 버튼을 중앙에 배치 */
  margin: 20px 0; /* 버튼 그룹의 위 아래 여백 */
}

.btn-custom {
  background-color: #f0c040; /* 부드러운 노란색 배경 */
  color: #fff; /* 텍스트 색상 */
  border: none; /* 기본 테두리 제거 */
  padding: 12px 20px; /* 버튼의 안쪽 여백 */
  margin: 0 5px; /* 버튼 사이의 간격 */
  border-radius: 5px; /* 모서리를 둥글게 */
  font-size: 16px; /* 텍스트 크기 */
  transition: background-color 0.3s ease, transform 0.3s ease; /* 부드러운 애니메이션 */
}

.btn-custom:hover {
  background-color: #e0b030; /* 호버 시 배경색 변경 (조금 더 어두운 노란색) */
  transform: translateY(-2px); /* 호버 시 약간 위로 이동 */
}

.btn-custom.active {
  background-color: #d0a020; /* 활성화된 버튼의 배경색 (더 진한 노란색) */
}

.form-group {
  margin-bottom: 1.5rem;
}

.active {
  background-color: #ffc107; /* 진한 노란색 */
  color: white;
}

.input-group-text {
  background-color: #ffc107;
  color: white;
}
</style>
