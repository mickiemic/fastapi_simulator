import json
import logging
from typing import Optional, List

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


router = APIRouter()
logger = logging.getLogger("fastapi_middleware_logger")

# ========= eTims VSCU Simulator ==================
class BhfReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    last_req_dt: str = Field(..., alias="lastReqDt")

    class Config:
        populate_by_name = True

@router.post("/branches/selectBranches")
async def select_branches(req: BhfReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /branches/selectBranches >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['branches/selectBranches']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /branches/selectBranches >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class CustReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    custm_tin: str = Field(..., alias="custmTin")

    class Config:
        populate_by_name = True

@router.post("/initializer/selectInitInfo")
async def select_init_info(req: BhfReq):
    try:
        jsonItem = jsonable_encoder(req)
        strPlayload = json.dumps(jsonItem)
        logger.info(f'>> /initializer/selectInitInfo >> {strPlayload}')
        with open('reqresp.json') as responses:
            _responses = json.load(responses)
            _vscu_messages = _responses.get('vscu_messages')
            _req_resp = _vscu_messages['initializer/selectInitInfo']
            if _req_resp.get('status') is True:
                _resp = _req_resp.get('response_success')
            else:
                _resp = _req_resp.get('response_fail')
            jsonResponse = json.loads(_resp)
        logger.info(f'<< /initializer/selectInitInfo >> {jsonResponse}')
        return JSONResponse(content=jsonResponse, status_code=201)
    except Exception as ex:
        strError = ex.with_traceback(None)
        # logger.error(strError)
        raise HTTPException(
            status_code=500,
            detail={
                "error": strError
            }
        )

@router.post("/customers/selectCustomer")
async def select_customer(req: CustReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /customers/selectCustomer >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['customers/selectCustomer']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /customers/selectCustomer >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

@router.post("/notices/selectNotices")
async def select_notices(req: BhfReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /notices/selectNotices >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['notices/selectNotices']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /notices/selectNotices >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

@router.post("/code/selectCodes")
async def select_codes(req: BhfReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /code/selectCodes >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['code/selectCodes']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /code/selectCodes >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

@router.post("/itemClass/selectItemsClass")
async def select_item_class(req: CustReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /itemClass/selectItemsClass >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['itemClass/selectItemsClass']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /itemClass/selectItemsClass >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class ImptItemReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    last_req_dt: str = Field(..., alias="lastReqDt")

    class Config:
        populate_by_name = True

@router.post("/imports/selectImportItems")
async def select_import_items(req: ImptItemReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /imports/selectImportItems >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['imports/selectImportItems']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /imports/selectImportItems >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

@router.post("/stock/selectStockItems")
async def select_stock_items(req: ImptItemReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /stock/selectStockItems >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['stock/selectStockItems']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /stock/selectStockItems >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

@router.post("/items/selectItems")
async def select_items(req: ImptItemReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /items/selectItems >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['items/selectItems']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /items/selectItems >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)


class TrnsPurchaseSalesReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    last_req_dt: str = Field(..., alias="lastReqDt")

    class Config:
        populate_by_name = True

@router.post("/trnsPurchase/selectTrnsPurchaseSales")
async def select_purchase_trxs(req: TrnsPurchaseSalesReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /trnsPurchase/selectTrnsPurchaseSales >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['trnsPurchase/selectTrnsPurchaseSales']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /trnsPurchase/selectTrnsPurchaseSales >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)


class BhfUserSaveReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    user_id: str = Field(..., alias="userId")
    user_nm: str = Field(..., alias="userNm")
    pwd: str
    adrs: Optional[str] = None
    cntc: Optional[str] = None
    auth_cd: Optional[str] = Field(None, alias="authCd")
    remark: Optional[str] = None
    use_yn: str = Field(..., alias="useYn")
    regr_nm: str = Field(..., alias="regrNm")
    regr_id: str = Field(..., alias="regrId")
    modr_nm: str = Field(..., alias="modrNm")
    modr_id: str = Field(..., alias="modrId")

    class Config:
        populate_by_name = True

@router.post("/branches/saveBrancheUsers")
async def save_branch_users(req: BhfUserSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /branches/saveBrancheUsers >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['branches/saveBrancheUsers']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /branches/saveBrancheUsers >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class BhfCustSaveReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    cust_no: str = Field(..., alias="custNo")
    cust_tin: str = Field(..., alias="custTin")
    cust_nm: str = Field(..., alias="custNm")
    adrs: Optional[str] = None
    tel_no: Optional[str] = Field(None, alias="telNo")
    email: Optional[str] = None
    fax_no: Optional[str] = Field(None, alias="faxNo")
    use_yn: str = Field(..., alias="useYn")
    remark: Optional[str] = None
    regr_nm: str = Field(..., alias="regrNm")
    regr_id: str = Field(..., alias="regrId")
    modr_nm: str = Field(..., alias="modrNm")
    modr_id: str = Field(..., alias="modrId")

    class Config:
        populate_by_name = True

@router.post("/branches/saveBrancheCustomers")
async def save_branch_customers(req: BhfCustSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /branches/saveBrancheCustomers >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['branches/saveBrancheCustomers']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /branches/saveBrancheCustomers >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class BhfInsuranceSaveReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    isrcc_cd: str = Field(..., alias="isrccCd")
    isrcc_nm: str = Field(..., alias="isrccNm")
    isrc_rt: int = Field(..., alias="isrcRt")
    use_yn: str = Field(..., alias="useYn")
    regr_nm: str = Field(..., alias="regrNm")
    regr_id: str = Field(..., alias="regrId")
    modr_nm: str = Field(..., alias="modrNm")
    modr_id: str = Field(..., alias="modrId")

    class Config:
        populate_by_name = True

@router.post("/branches/saveBrancheInsurances")
async def save_branch_insurances(req: BhfInsuranceSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /branches/saveBrancheInsurances >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['branches/saveBrancheInsurances']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /branches/saveBrancheInsurances >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class ItemSaveReq(BaseModel):
    item_cd: str = Field(..., alias="itemCd")
    item_cls_cd: str = Field(..., alias="itemClsCd")
    item_ty_cd: str = Field(..., alias="itemTyCd")
    item_nm: str = Field(..., alias="itemNm")
    item_std_nm: str = Field(..., alias="itemStdNm")
    orgn_nat_cd: str = Field(..., alias="orgnNatCd")
    pkg_unit_cd: str = Field(..., alias="pkgUnitCd")
    qty_unit_cd: str = Field(..., alias="qtyUnitCd")
    tax_ty_cd: str = Field(..., alias="taxTyCd")
    btch_no: Optional[str] = Field(None, alias="btchNo")
    bcd: Optional[str] = None
    dft_prc: int = Field(..., alias="dftPrc")
    grp_prc_l1: int = Field(..., alias="grpPrcL1")
    grp_prc_l2: int = Field(..., alias="grpPrcL2")
    grp_prc_l3: int = Field(..., alias="grpPrcL3")
    grp_prc_l4: int = Field(..., alias="grpPrcL4")
    grp_prc_l5: Optional[str] = Field(None, alias="grpPrcL5")
    add_info: str = Field(..., alias="addInfo")
    sfty_qty: Optional[str] = Field(None, alias="sftyQty")
    isrc_aplcb_yn: str = Field(..., alias="isrcAplcbYn")
    use_yn: str = Field(..., alias="useYn")
    regr_nm: str = Field(..., alias="regrNm")
    regr_id: str = Field(..., alias="regrId")
    modr_nm: str = Field(..., alias="modrNm")
    modr_id: str = Field(..., alias="modrId")
    tin: str
    bhf_id: str = Field(..., alias="bhfId")

    class Config:
        populate_by_name = True

@router.post("/items/saveItems")
async def save_items(req: ItemSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /items/saveItems >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['items/saveItems']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /items/saveItems >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class ItemCpstSaveReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    item_cd: str = Field(..., alias="itemCd")
    cpst_item_cd: str = Field(..., alias="cpstItemCd")
    cpst_qty: int = Field(..., alias="cpstQty")
    regr_id: str = Field(..., alias="regrId")
    regr_nm: str = Field(..., alias="regrNm")

    class Config:
        populate_by_name = True

@router.post("/items/saveItemComposition")
async def save_item_composition(req: ItemCpstSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /items/saveItemComposition >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['items/saveItemComposition']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /items/saveItemComposition >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class StockMstSaveReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    item_cd: str = Field(..., alias="itemCd")
    rsd_qty: int = Field(..., alias="rsdQty")
    regr_id: str = Field(..., alias="regrId")
    regr_nm: str = Field(..., alias="regrNm")
    modr_nm: str = Field(..., alias="modrNm")
    modr_id: str = Field(..., alias="modrId")

    class Config:
        populate_by_name = True

@router.post("/stockMaster/saveStockMaster")
async def save_stock_master(req: StockMstSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /stockMaster/saveStockMaster >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['stockMaster/saveStockMaster']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /stockMaster/saveStockMaster >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class ImptItemSaveReq(BaseModel):
    tin: str
    bhf_id: str = Field(..., alias="bhfId")
    task_cd: str = Field(..., alias="taskCd")
    dcl_de: str = Field(..., alias="dclDe")
    item_seq: int = Field(..., alias="itemSeq")
    hs_cd: str = Field(..., alias="hsCd")
    item_cls_cd: str = Field(..., alias="itemClsCd")
    item_cd: str = Field(..., alias="itemCd")
    impt_item_stts_cd: str = Field(..., alias="imptItemSttsCd")
    remark: str
    modr_nm: str = Field(..., alias="modrNm")
    modr_id: str = Field(..., alias="modrId")

    class Config:
        populate_by_name = True

@router.post("/imports/updateImportItems")
async def update_import_items(req: ImptItemSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /imports/updateImportItems >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['imports/updateImportItems']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /imports/updateImportItems >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class StockIOItem(BaseModel):
    tot_dc_amt: float = Field(..., alias="totDcAmt")
    item_expr_dt: Optional[str] = Field(None, alias="itemExprDt")
    item_seq: int = Field(..., alias="itemSeq")
    item_cd: str = Field(..., alias="itemCd")
    item_ty_cd: str = Field(..., alias="itemTyCd")
    item_cls_cd: str = Field(..., alias="itemClsCd")
    item_nm: str = Field(..., alias="itemNm")
    pkg_unit_cd: str = Field(..., alias="pkgUnitCd")
    pkg: int
    qty_unit_cd: str = Field(..., alias="qtyUnitCd")
    qty: int
    bcd: Optional[str] = None
    tax_ty_cd: str = Field(..., alias="taxTyCd")
    prc: float
    sply_amt: float = Field(..., alias="splyAmt")
    taxbl_amt: float = Field(..., alias="taxblAmt")
    tax_amt: float = Field(..., alias="taxAmt")
    tot_amt: float = Field(..., alias="totAmt")

    class Config:
        populate_by_name = True

class StockIOSaveReq(BaseModel):
    sar_no: int = Field(..., alias="sarNo")
    org_sar_no: int = Field(..., alias="orgSarNo")
    reg_ty_cd: str = Field(..., alias="regTyCd")
    cust_tin: str = Field(..., alias="custTin")
    cust_nm: str = Field(..., alias="custNm")
    cust_bhf_id: str = Field(..., alias="custBhfId")
    sar_ty_cd: str = Field(..., alias="sarTyCd")
    ocrn_dt: str = Field(..., alias="ocrnDt")
    tot_item_cnt: int = Field(..., alias="totItemCnt")
    tot_taxbl_amt: float = Field(..., alias="totTaxblAmt")
    tot_tax_amt: float = Field(..., alias="totTaxAmt")
    tot_amt: float = Field(..., alias="totAmt")
    remark: str
    regr_id: str = Field(..., alias="regrId")
    regr_nm: str = Field(..., alias="regrNm")
    modr_id: str = Field(..., alias="modrId")
    modr_nm: str = Field(..., alias="modrNm")
    item_list: List[StockIOItem] = Field(..., alias="itemList")
    tin: str
    bhf_id: str = Field(..., alias="bhfId")

    class Config:
        populate_by_name = True

@router.post("/saveStockItems/saveStockItems")
async def save_stock_items(req: StockIOSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /saveStockItems/saveStockItems >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['saveStockItems/saveStockItems']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /saveStockItems/saveStockItems >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class Receipt(BaseModel):
    cust_tin: str = Field(..., alias="custTin")
    cust_mbl_no: str = Field(..., alias="custMblNo")
    rpt_no: int = Field(..., alias="rptNo")
    trde_nm: str = Field(..., alias="trdeNm")
    adrs: str
    top_msg: Optional[str] = Field(None, alias="topMsg")
    btm_msg: Optional[str] = Field(None, alias="btmMsg")
    prchr_acptc_yn: str = Field(..., alias="prchrAcptcYn")

    class Config:
        populate_by_name = True

class SalesItem(BaseModel):
    dc_rt: int = Field(..., alias="dcRt")
    dc_amt: float = Field(..., alias="dcAmt")
    isrcc_cd: Optional[str] = Field(None, alias="isrccCd")
    isrcc_nm: Optional[str] = Field(None, alias="isrccNm")
    isrc_rt: Optional[str] = Field(None, alias="isrcRt")
    isrc_amt: Optional[str] = Field(None, alias="isrcAmt")
    item_seq: int = Field(..., alias="itemSeq")
    item_cd: str = Field(..., alias="itemCd")
    item_ty_cd: str = Field(..., alias="itemTyCd")
    item_cls_cd: str = Field(..., alias="itemClsCd")
    item_nm: str = Field(..., alias="itemNm")
    pkg_unit_cd: str = Field(..., alias="pkgUnitCd")
    pkg: int
    qty_unit_cd: str = Field(..., alias="qtyUnitCd")
    qty: int
    bcd: Optional[str] = None
    tax_ty_cd: str = Field(..., alias="taxTyCd")
    prc: float
    sply_amt: float = Field(..., alias="splyAmt")
    taxbl_amt: float = Field(..., alias="taxblAmt")
    tax_amt: float = Field(..., alias="taxAmt")
    tot_amt: float = Field(..., alias="totAmt")

    class Config:
        populate_by_name = True

class TrnsSalesSaveReq(BaseModel):
    trd_invc_no: str = Field(..., alias="trdInvcNo")
    invc_no: int = Field(..., alias="invcNo")
    org_invc_no: int = Field(..., alias="orgInvcNo")
    cust_tin: str = Field(..., alias="custTin")
    cust_nm: str = Field(..., alias="custNm")
    sales_ty_cd: str = Field(..., alias="salesTyCd")
    rcpt_ty_cd: str = Field(..., alias="rcptTyCd")
    pmt_ty_cd: str = Field(..., alias="pmtTyCd")
    sales_stts_cd: str = Field(..., alias="salesSttsCd")
    cfm_dt: str = Field(..., alias="cfmDt")
    sales_dt: str = Field(..., alias="salesDt")
    stock_rls_dt: str = Field(..., alias="stockRlsDt")
    cncl_req_dt: Optional[str] = Field(None, alias="cnclReqDt")
    cncl_dt: Optional[str] = Field(None, alias="cnclDt")
    rfd_dt: Optional[str] = Field(None, alias="rfdDt")
    rfd_rsn_cd: Optional[str] = Field(None, alias="rfdRsnCd")
    tot_item_cnt: int = Field(..., alias="totItemCnt")
    taxbl_amt_a: int = Field(..., alias="taxblAmtA")
    taxbl_amt_b: float = Field(..., alias="taxblAmtB")
    taxbl_amt_c: int = Field(..., alias="taxblAmtC")
    taxbl_amt_d: int = Field(..., alias="taxblAmtD")
    taxbl_amt_e: int = Field(..., alias="taxblAmtE")
    tax_rt_a: int = Field(..., alias="taxRtA")
    tax_rt_b: int = Field(..., alias="taxRtB")
    tax_rt_c: int = Field(..., alias="taxRtC")
    tax_rt_d: int = Field(..., alias="taxRtD")
    tax_rt_e: int = Field(..., alias="taxRtE")
    tax_amt_a: int = Field(..., alias="taxAmtA")
    tax_amt_b: float = Field(..., alias="taxAmtB")
    tax_amt_c: int = Field(..., alias="taxAmtC")
    tax_amt_d: int = Field(..., alias="taxAmtD")
    tax_amt_e: int = Field(..., alias="taxAmtE")
    tot_taxbl_amt: float = Field(..., alias="totTaxblAmt")
    tot_tax_amt: float = Field(..., alias="totTaxAmt")
    tot_amt: float = Field(..., alias="totAmt")
    prchr_acptc_yn: str = Field(..., alias="prchrAcptcYn")
    remark: str
    regr_id: str = Field(..., alias="regrId")
    regr_nm: str = Field(..., alias="regrNm")
    modr_id: str = Field(..., alias="modrId")
    modr_nm: str = Field(..., alias="modrNm")
    receipt: Receipt
    item_list: List[SalesItem] = Field(..., alias="itemList")
    tin: str
    bhf_id: str = Field(..., alias="bhfId")

    class Config:
        populate_by_name = True

@router.post("/trnsSales/saveSales")
async def trnsSales_save_sales(req: TrnsSalesSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /trnsSales/saveSales >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['trnsSales/saveSales']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /trnsSales/saveSales >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

class PurchaseItem(BaseModel):
    spplr_item_cls_cd: str = Field(..., alias="spplrItemClsCd")
    spplr_item_cd: str = Field(..., alias="spplrItemCd")
    spplr_item_nm: str = Field(..., alias="spplrItemNm")
    dc_rt: int = Field(..., alias="dcRt")
    dc_amt: int = Field(..., alias="dcAmt")
    item_expr_dt: Optional[str] = Field(None, alias="itemExprDt")
    item_seq: int = Field(..., alias="itemSeq")
    item_cd: str = Field(..., alias="itemCd")
    item_ty_cd: str = Field(..., alias="itemTyCd")
    item_cls_cd: str = Field(..., alias="itemClsCd")
    item_nm: str = Field(..., alias="itemNm")
    pkg_unit_cd: str = Field(..., alias="pkgUnitCd")
    pkg: int
    qty_unit_cd: str = Field(..., alias="qtyUnitCd")
    qty: int
    bcd: Optional[str] = None
    tax_ty_cd: str = Field(..., alias="taxTyCd")
    prc: int
    sply_amt: int = Field(..., alias="splyAmt")
    taxbl_amt: int = Field(..., alias="taxblAmt")
    tax_amt: int = Field(..., alias="taxAmt")
    tot_amt: int = Field(..., alias="totAmt")

    class Config:
        populate_by_name = True

class TrnsPurchaseSaveReq(BaseModel):
    invc_no: int = Field(..., alias="invcNo")
    org_invc_no: int = Field(..., alias="orgInvcNo")
    spplr_tin: Optional[str] = Field(None, alias="spplrTin")
    spplr_bhf_id: Optional[str] = Field(None, alias="spplrBhfId")
    spplr_nm: Optional[str] = Field(None, alias="spplrNm")
    spplr_invc_no: Optional[str] = Field(None, alias="spplrInvcNo")
    reg_ty_cd: str = Field(..., alias="regTyCd")
    pchs_ty_cd: str = Field(..., alias="pchsTyCd")
    rcpt_ty_cd: str = Field(..., alias="rcptTyCd")
    pmt_ty_cd: str = Field(..., alias="pmtTyCd")
    pchs_stts_cd: str = Field(..., alias="pchsSttsCd")
    cfm_dt: Optional[str] = Field(None, alias="cfmDt")
    pchs_dt: str = Field(..., alias="pchsDt")
    wrhs_dt: str = Field(..., alias="wrhsDt")
    cncl_req_dt: Optional[str] = Field(None, alias="cnclReqDt")
    cncl_dt: Optional[str] = Field(None, alias="cnclDt")
    rfd_dt: Optional[str] = Field(None, alias="rfdDt")
    tot_item_cnt: int = Field(..., alias="totItemCnt")
    taxbl_amt_a: int = Field(..., alias="taxblAmtA")
    taxbl_amt_b: int = Field(..., alias="taxblAmtB")
    taxbl_amt_c: int = Field(..., alias="taxblAmtC")
    taxbl_amt_d: int = Field(..., alias="taxblAmtD")
    taxbl_amt_e: int = Field(..., alias="taxblAmtE")
    tax_rt_a: int = Field(..., alias="taxRtA")
    tax_rt_b: int = Field(..., alias="taxRtB")
    tax_rt_c: int = Field(..., alias="taxRtC")
    tax_rt_d: int = Field(..., alias="taxRtD")
    tax_rt_e: int = Field(..., alias="taxRtE")
    tax_amt_a: int = Field(..., alias="taxAmtA")
    tax_amt_b: int = Field(..., alias="taxAmtB")
    tax_amt_c: int = Field(..., alias="taxAmtC")
    tax_amt_d: int = Field(..., alias="taxAmtD")
    tax_amt_e: int = Field(..., alias="taxAmtE")
    tot_taxbl_amt: int = Field(..., alias="totTaxblAmt")
    tot_tax_amt: int = Field(..., alias="totTaxAmt")
    tot_amt: int = Field(..., alias="totAmt")
    remark: str
    regr_id: str = Field(..., alias="regrId")
    regr_nm: str = Field(..., alias="regrNm")
    modr_id: str = Field(..., alias="modrId")
    modr_nm: str = Field(..., alias="modrNm")
    item_list: List[PurchaseItem] = Field(..., alias="itemList")
    tin: str
    bhf_id: str = Field(..., alias="bhfId")

    class Config:
        populate_by_name = True

@router.post("/trnsPurchase/savePurchases")
async def trnsPurchase_save_purchases(req: TrnsPurchaseSaveReq):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /trnsPurchase/savePurchases >> {strPlayload}')
    with open('reqresp.json') as responses:
        _responses = json.load(responses)
        _vscu_messages = _responses.get('vscu_messages')
        _req_resp = _vscu_messages['trnsPurchase/savePurchases']
        if _req_resp.get('status') is True:
            _resp = _req_resp.get('response_success')
        else:
            _resp = _req_resp.get('response_fail')
        jsonResponse = json.loads(_resp)
    logger.info(f'<< /trnsPurchase/savePurchases >> {jsonResponse}')
    return JSONResponse(content=jsonResponse, status_code=201)

