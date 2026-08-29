import styles from "./show.module.css"
function ShowAlert({func}){
    return<div className={`${styles.container} ${styles.snow}`}>
        good to see you 
        <span onClick={func}>❌</span>
    </div>
}
export default ShowAlert