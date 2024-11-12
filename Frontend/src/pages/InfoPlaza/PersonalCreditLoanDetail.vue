<template>
  <div>
    <InfoPlazaHeader />

    <div class="custom-container">
      <div class="row">
        <!-- Signle job content-->
        <div
          class="col-lg-6 position-relative pe-lg-5 mb-5 mb-lg-0"
          style="z-index: 1025"
        >
          <div class="d-flex justify-content-between mb-2">
            <div class="d-flex align-items-center">
              <div class="d-flex align-items-center me-5">
                <img
                  :src="'/images/banklogo/' + data.korCoNm + '.png'"
                  alt=""
                  style="width: 50px"
                />
              </div>
              <div class="d-flex align-items-center">
                <div class="text-left">
                  <span class="fs-2 text-gray-500 fw-bolder d-block">
                    {{ data.finPrdtNm }}
                  </span>
                </div>
              </div>
            </div>
            <div class="text-end">
              <span class="badge bg-faded-accent rounded-pill mt-5">{{
                data.crdtPrdtTypeNm
              }}</span>
            </div>
          </div>
          <ul class="list-unstyled fs-sm ms-1 mb-4">
            <li class="mb-2">
              <i class="fa-solid fa-house-user text-muted me-2"></i
              ><span>{{ data.korCoNm }}</span>
            </li>
            <li class="d-flex align-items-center mb-2">
              <i class="fa-solid fa-calendar-days text-muted me-2"></i
              ><span
                >{{ formatDate(data.dclsStrtDay) }} ~
                {{ formatEndDate(data.dclsEndDay) }}</span
              >
            </li>
            <li class="d-flex align-items-center mb-2">
              <i class="fa-solid fa-coins text-muted me-2"></i
              ><span>{{ data.crdtGradAvg }}%</span>
            </li>
          </ul>
          <hr class="mb-4" />

          <h3 class="h5 pt-2">신용 점수별 금리</h3>
          <ul class="list-unstyled">
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">900점 초과</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad1 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">801~900점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad4 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">701~800점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad5 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">601~700점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad6 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">501~600점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad10 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">401~500점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad11 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">401~500점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad11 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">301~400점</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad12 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">300점 이하</span>
              <span class="colon">: </span>
              <span class="ms-1">{{ data.crdtGrad13 }}%</span>
            </li>
          </ul>
        </div>
        <div class="col-1" style="z-index: 1025"></div>
        <!-- Sticky sidebar-->
        <LoanRateCalculate
          :defaultActiveButton="'left'"
          :endpoint="'/getFilteredCreditLoanList'"
        />
      </div>
      <div class="text-center mt-10 mb-5">
        <RouterLink
          :to="`/infoPlaza/personalCreditLoan/`"
          class="btn btn-sm btn-neutral mb-5 mt-1"
          >목록</RouterLink
        >
      </div>
      <div class="row mt-5">
        <h3>이 대출 상품이 마음에 드시나요?</h3>
        <div class="row mt-5">
          <!-- 카드 여러 개 -->
          <swiper
            :slides-per-view="3"
            :space-between="50"
            :navigation="true"
            :pagination="false"
            :modules="modules"
            :preventClicks="false"
            :preventClicksPropagation="false"
            style="padding-left: 70px; padding-right: 70px"
          >
            <swiper-slide v-for="(item, index) in recommandList" :key="index">
              <div @click="navigateToDetail(item.id)">
                <RouterLink
                  :to="`/infoPlaza/personalCreditLoan/personalCreditLoanDetail/${item.id}`"
                >
                  <div class="card card-xl-stretch h-100 hover-card">
                    <div
                      class="card-body pt-5 d-flex flex-column justify-content-between"
                    >
                      <div>
                        <div class="d-flex flex-stack flex-wrap">
                          <span
                            class="fs-3 text-gray-500 pe-2"
                            style="font-weight: 500"
                          >
                            <div class="row mb-3" style="height: 70px">
                              <div class="col-4 d-flex align-items-center">
                                <img
                                  :src="
                                    '/images/banklogo/' + item.korCoNm + '.png'
                                  "
                                  alt=""
                                  style="width: 100px"
                                />
                              </div>
                              <div class="col-8 d-flex align-items-center">
                                <!-- Change align-items to center -->
                                <span
                                  class="fs-3 text-gray-500 fw-bolder pe-2 text-left text-truncate"
                                >
                                  {{ item.korCoNm }}
                                </span>
                              </div>
                            </div>
                            <div class="d-flex flex-stack flex-wrap">
                              <span
                                class="fs-3 text-gray-500 pe-2 text-truncate"
                                style="font-weight: 500; width: 220px"
                              >
                                {{ item.finPrdtNm }}
                              </span>
                            </div>
                          </span>
                        </div>
                        <div class="carousel-inner pt-6">
                          <div class="carousel-item active">
                            <div class="carousel-wrapper">
                              <div class="d-flex flex-column flex-grow-1">
                                <!-- 콘텐츠 추가 가능 -->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- 금리 -->
                      <div
                        class="d-flex justify-content-end align-items-end ms-auto"
                      >
                        <p class="fs-6 text-gray-600 mb-1">금리</p>
                        <p class="h2 fw-bold mb-0 ms-2">
                          {{ item.crdtGradAvg }} %
                        </p>
                      </div>
                    </div>
                  </div>
                </RouterLink>
              </div>
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import { useRoute, useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, Pagination, Navigation } from 'swiper/modules';
import LoanRateCalculate from '@/components/infoplaza/LoanRateCalculate.vue';
import 'swiper/css';
import 'swiper/css/bundle';
import 'swiper/css/a11y';
import 'swiper/css/autoplay';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

const modules = [Autoplay, Pagination, Navigation];

const route = useRoute();
const router = useRouter();

// 수동 라우팅 함수
const navigateToDetail = (id) => {
  router.push(`/infoPlaza/personalCreditLoan/personalCreditLoanDetail/${id}`);
  window.location.reload();
};

const id = ref('');
id.value = route.params.id;
const BASEURI = '/api/infoPlaza/loan';

const data = ref();
const recommandList = ref();

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getDetailItemCreditLoan', {
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

// 데이터 리스트 가져오는 함수
const bringRecommandList = async () => {
  try {
    // Best 인기 업종 - 전체
    console.log(data.value);
    const response = await axios.get(BASEURI + '/getFilteredCreditLoanList', {
      params: {
        companyName: '전체',
        type: data.value.crdtPrdtTypeNm,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      recommandList.value = response.data;
      console.log(recommandList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 날짜 형식 변환
const formatDate = (date) => {
  const dateString = String(date);
  if (dateString.length !== 8) {
    return dateString;
  }

  const year = dateString.substring(0, 4);
  const month = dateString.substring(4, 6);
  const day = dateString.substring(6, 8);

  return `${year.substring(2)}/${month}/${day}`;
};

// dclsEndDay가 null일 경우를 처리하는 함수
const formatEndDate = (date) => {
  if (date === null) {
    return '';
  }
  return formatDate(date);
};

// bringDataList가 완료된 후 bringRecommandList 호출
const fetchData = async () => {
  await bringDataList(); // bringDataList가 완료되기를 기다림
  await bringRecommandList(); // bringRecommandList 실행
};

// fetchData 호출
fetchData();
</script>

<style scoped>
.hover-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-card:hover {
  transform: translate(
    -3px,
    -3px
  ); /* Moves the card slightly to the top-left */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow effect */
}
.text-truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.content-box {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}
.content-item {
  display: flex;
  margin-bottom: 8px;
}
.label {
  min-width: 100px; /* Ensure labels align properly */
  color: #333;
}
.value {
  color: #555;
}
.colon {
  padding-right: 0px; /* Optional additional spacing */
}

.badge {
  --fi-badge-padding-x: 0.75em;
  --fi-badge-padding-y: 0.4375em;
  --fi-badge-font-size: 0.8125em;
  --fi-badge-font-weight: 600;
  --fi-badge-color: black;
  --fi-badge-border-radius: 0.375rem;
  display: inline-block;
  padding: var(--fi-badge-padding-y) var(--fi-badge-padding-x);
  font-size: var(--fi-badge-font-size);
  font-weight: var(--fi-badge-font-weight);
  line-height: 1;
  color: var(--fi-badge-color);
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: var(--fi-badge-border-radius);
}

.bg-faded-accent {
  background-color: rgba(80, 43, 246, 0.2) !important; /* 더 진한 배경색 */
}

.rounded-pill {
  border-radius: 50rem !important;
}
.custom-container {
  max-width: 1100px; /* 원하는 너비로 설정 */
  margin: 0 auto; /* 가운데 정렬 */
}
</style>
